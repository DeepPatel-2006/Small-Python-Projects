# File: RA_01.py         
# Author:  Deep Patel    
# Section: 3R
# E-mail:  djp6412@psu.edu
# Temperature Coverter 
fahrenheit = float(input("Enter temperature in F: "))
FAHRENHEIT_TO_CELSIUS = 5/9
TEMP_CONSTANT = 32
celsius = (fahrenheit - TEMP_CONSTANT) * FAHRENHEIT_TO_CELSIUS
print(fahrenheit, "F is equivalent to", celsius, "C")

# Weekly Commute
num_miles = float(input("Number of miles for one-way trip: "))
num_days = int(input("Worked days: "))
SPEED = 55
distance = num_days * num_miles * 2
time = distance / SPEED
print("The number of miles driven in a week is", distance)
print("The number of hours spent in the car is", time)
