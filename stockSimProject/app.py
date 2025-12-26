from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import requests
from datetime import datetime
import pandas as pd
import time

app = Flask(__name__)
app.secret_key = "your_secret_key"
DB_PATH = "users.db"

# --- Alpha Vantage Setup ---
API_KEY = "6C0WM7609FRGV5Z5"  # <-- replace with your API key
BASE_URL = "https://www.alphavantage.co/query"

# ---------------- Database Setup ----------------
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                balance REAL DEFAULT 25000,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS portfolio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                ticker TEXT NOT NULL,
                shares REAL NOT NULL,
                buy_date TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.commit()
init_db()

# ---------------- Stock Helpers ----------------
cache = {}  # Simple in-memory cache for stock data

def get_stock_data(ticker):
    """Get current stock data from Alpha Vantage with 60s cache"""
    now = time.time()
    if ticker in cache:
        ts, data = cache[ticker]
        if now - ts < 60:  # use cached value if <60s old
            return data
    try:
        url = f"{BASE_URL}?function=GLOBAL_QUOTE&symbol={ticker}&apikey={API_KEY}"
        r = requests.get(url)
        data = r.json().get("Global Quote", {})
        if not data:
            return None
        result = {
            "symbol": ticker.upper(),
            "price": round(float(data.get("05. price", 0)), 2),
            "open": round(float(data.get("02. open", 0)), 2),
            "high": round(float(data.get("03. high", 0)), 2),
            "low": round(float(data.get("04. low", 0)), 2)
        }
        cache[ticker] = (now, result)
        return result
    except Exception:
        return None

def get_stock_history(ticker, limit=365, full=False):
    """Get daily time series for up to 'limit' days (or full history if requested)."""
    try:
        size = "full" if full else "compact"
        url = f"{BASE_URL}?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&outputsize={size}&apikey={API_KEY}"
        r = requests.get(url)
        data = r.json().get("Time Series (Daily)", {})
        if not data:
            return None
        df = pd.DataFrame(data).T
        df = df.rename(columns=lambda x: x.lower())
        df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        return df.tail(limit) if limit else df
    except Exception:
        return None

def get_portfolio_history(user_id):
    """Reconstruct portfolio value over time using buy dates and cash."""
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT balance, created_at FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        if not row:
            return [], []
        current_cash, created_at = row
        created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        c.execute("SELECT ticker, shares, buy_date FROM portfolio WHERE user_id = ?", (user_id,))
        rows = c.fetchall()

    if not rows:
        return [created_at.strftime("%Y-%m-%d")], [round(current_cash, 2)]

    all_hist = pd.DataFrame()
    buy_dates = []

    for ticker, shares, buy_date in rows:
        hist = get_stock_history(ticker, limit=365)
        if hist is None:
            continue
        series = hist["4. close"].astype(float) * shares
        series.name = ticker
        buy_date_dt = datetime.strptime(buy_date, "%Y-%m-%d")
        series.loc[series.index < buy_date_dt] = 0
        buy_dates.append(buy_date_dt)
        all_hist = pd.concat([all_hist, series], axis=1)

    if all_hist.empty:
        return [], []

    all_hist = all_hist.fillna(0)
    total_series = all_hist.sum(axis=1)
    total_series.iloc[-1] += current_cash
    first_buy = min(buy_dates) if buy_dates else None
    start_date = min(first_buy, created_at) if first_buy else created_at
    total_series = total_series[total_series.index >= start_date]

    dates = [d.strftime("%Y-%m-%d") for d in total_series.index]
    values = [round(v, 2) for v in total_series.values]
    return dates, values

# ---------------- Routes ----------------
@app.route("/", methods=["GET"])
def home():
    if "user_id" not in session:
        return redirect(url_for("login"))

    user_id = session["user_id"]
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        balance = row[0] if row else 0

        c.execute("SELECT ticker, shares FROM portfolio WHERE user_id = ?", (user_id,))
        portfolio_rows = c.fetchall()

        portfolio = []
        for row in portfolio_rows:
            stock_data = get_stock_data(row[0])
            portfolio.append({
                "ticker": row[0],
                "shares": row[1],
                "price": stock_data["price"] if stock_data else None,
                "open": stock_data["open"] if stock_data else None,
                "high": stock_data["high"] if stock_data else None,
                "low": stock_data["low"] if stock_data else None
            })

    tickers = ["AAPL", "TSLA", "MSFT"]
    stocks = []
    for t in tickers:
        stock_data = get_stock_data(t)
        if stock_data:
            stocks.append(stock_data)

    portfolio_dates, portfolio_values = get_portfolio_history(user_id)

    return render_template("home.html",
                           email=session["email"],
                           balance=balance,
                           portfolio=portfolio,
                           stocks=stocks,
                           portfolio_dates=portfolio_dates,
                           portfolio_values=portfolio_values)
    
# ---------------- API for lazy-loading stock prices ----------------
@app.route("/api/stock/<ticker>")
def api_stock(ticker):
    stock = get_stock_data(ticker)
    if stock:
        return jsonify(stock)
    return jsonify({"error": "Stock not found"}), 404

@app.route("/search")
def search():
    query = request.args.get("q", "").upper()
    all_tickers = ["AAPL", "TSLA", "MSFT", "GOOG", "AMZN", "NVDA", "NFLX"]
    suggestions = [t for t in all_tickers if query in t]
    return jsonify(suggestions)

@app.route("/stock/<ticker>")
def stock_detail(ticker):
    if "user_id" not in session:
        return redirect(url_for("login"))

    period = request.args.get("period", "7d")
    period_map = {"1d":1, "7d":7, "1mo":30, "6mo":180, "1y":365, "5y":1825, "max":None}
    full = True if period in ["1y","5y","max"] else False
    limit = period_map.get(period,30)

    user_id = session["user_id"]
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        row = c.fetchone()
        balance = row[0] if row else 0

    hist = get_stock_history(ticker, limit=limit, full=full)
    if hist is None or hist.empty:
        flash("Stock data not available!", "danger")
        return redirect(url_for("home"))

    dates = [d.strftime("%Y-%m-%d") for d in hist.index]
    closes = [round(float(c),2) for c in hist["4. close"]]
    latest = hist.iloc[-1]
    data = {
        "symbol": ticker.upper(),
        "price": round(float(latest["4. close"]),2),
        "open": round(float(latest["1. open"]),2),
        "high": round(float(latest["2. high"]),2),
        "low": round(float(latest["3. low"]),2)
    }

    return render_template("stock_detail.html",
                           stock=data,
                           email=session["email"],
                           balance=balance,
                           chart_labels=dates,
                           chart_data=closes,
                           current_period=period)

# ---------------- Trade Routes ----------------
@app.route("/trade/<action>/<ticker>", methods=["POST"])
def trade_stock(action, ticker):
    if "user_id" not in session:
        return redirect(url_for("login"))

    shares = float(request.form.get("shares",0))
    if shares <=0:
        flash("Invalid number of shares", "danger")
        return redirect(url_for("stock_detail", ticker=ticker))

    user_id = session["user_id"]
    with sqlite3.connect(DB_PATH, timeout=10) as conn:
        c = conn.cursor()
        stock = get_stock_data(ticker)
        if not stock:
            flash("Stock not available", "danger")
            return redirect(url_for("stock_detail", ticker=ticker))
        price = stock["price"]

        c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
        balance = c.fetchone()[0]

        c.execute("SELECT id, shares FROM portfolio WHERE user_id = ? AND ticker = ?", (user_id, ticker))
        row = c.fetchone()

        today = datetime.today().strftime("%Y-%m-%d")

        if action=="buy":
            total_cost = price*shares
            if total_cost>balance:
                flash("Insufficient funds","danger")
            else:
                balance -= total_cost
                if row:
                    c.execute("UPDATE portfolio SET shares = shares + ? WHERE id = ?", (shares,row[0]))
                else:
                    c.execute("INSERT INTO portfolio (user_id,ticker,shares,buy_date) VALUES (?,?,?,?)",
                              (user_id,ticker,shares,today))
                c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance,user_id))
                flash(f"Bought {shares} shares of {ticker} for ${total_cost}","success")
        elif action=="sell":
            if not row or row[1]<shares:
                flash("Not enough shares to sell","danger")
            else:
                total_value = price*shares
                balance += total_value
                new_shares = row[1]-shares
                if new_shares>0:
                    c.execute("UPDATE portfolio SET shares = ? WHERE id = ?", (new_shares,row[0]))
                else:
                    c.execute("DELETE FROM portfolio WHERE id = ?", (row[0],))
                c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance,user_id))
                flash(f"Sold {shares} shares of {ticker} for ${total_value}","success")
        conn.commit()
    return redirect(url_for("stock_detail", ticker=ticker))

# ---------------- Auth Routes ----------------
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        hashed_pw = generate_password_hash(password)
        try:
            with sqlite3.connect(DB_PATH) as conn:
                c = conn.cursor()
                c.execute("INSERT INTO users (email,password,balance) VALUES (?,?,?)",
                          (email,hashed_pw,25000))
                conn.commit()
            flash("Signup successful! Please log in.","success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            flash("Email already exists!","danger")
    return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        with sqlite3.connect(DB_PATH) as conn:
            c = conn.cursor()
            c.execute("SELECT id,password FROM users WHERE email = ?", (email,))
            user = c.fetchone()
        if user and check_password_hash(user[1],password):
            session["user_id"]=user[0]
            session["email"]=email
            flash("Logged in successfully!","success")
            return redirect(url_for("home"))
        else:
            flash("Invalid email or password","danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.","info")
    return redirect(url_for("login"))

# ---------------- Run ----------------
if __name__=="__main__":
    app.run(debug=True)
