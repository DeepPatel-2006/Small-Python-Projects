"""
Course  : CMPSC 131, Fall 2024
File    : PS1.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006

Collaboration Statement: 
"""

#-YOUR CODE STARTS HERE  (TODO) 
def math_func_1(x: int) -> float:
    answer: float = ((10 * x - 3) / 8) * (7 / (4 * x - 3))
    return answer



def math_func_2(a: int, b: int, c: int) -> float:
    answer: float = ((2 % a - 3) / (c * b)) + (4 // c) - b
    return answer


def m_to_arshins(meters : float | int) -> float:
    """
        Converts the given amount of meters into arshins
        
        Args:
            meters (float): the amount of meters that convert into arshins
        
        Returns:
            arshins (float): the amount of arshins in given meters
    """
    ARSHINS_PER_METER: float = 1.406
    arshins: float = meters * ARSHINS_PER_METER
    return arshins

def convert_min(minutes: int) -> int:
    """
        Converts the given amount of minutes into  a combination of years and days
    
        Args:
            minutes (int): the amount of minutes that convert into years and days
        
        Displays:
            x min = y year(s) and z day(s), where x is the input minutes, y is the amount of years in minutes, z is the amount amount of days in minutes
    """
    MINUTES_PER_DAY: int = 1440
    DAYS_PER_YEAR: int = 365
    total_days: int = minutes // MINUTES_PER_DAY
    years = total_days // DAYS_PER_YEAR
    days = total_days % 365
    print(minutes, "min =", years, "year(s) and", days, "day(s)")
    return 1


def calc_final_price(price: float | int, tax: int) -> float:
    """ 
        Calculates final price after tax based on price and tax rate
        
        Args:
            price (float): the cost of the item 
            tax (int): the tax rate as a whole number. Example 6% tax rate = 6
        
        Returns:
            final_price (float): the final cost after tax is applied
    """
    tax_in_decimal: float = tax / 100
    final_price: float = price + price * tax_in_decimal
    return final_price


def get_displacement(initital_velocity: float | int, acceleration: float | int, time: float | int) -> float:
    """
        Calculates displacement in meters from the given initial_velocity in m/s, acceleration in m/s^2, and time in seconds
        
        Args:
            initial_velocty (float | int): the initial velocity in m/s of the moving body
            acceleration(float | int): the uniform acceleration in m/s^2  of the moving body
            time (float | int): the given time in seconds in which the displacement is calculated
        
        Returns:
            displacement(float): the displacement the object experienced
    """
    dispacement: float = (initital_velocity * time) + (0.5 * acceleration * time ** 2)
    return dispacement
    
def p_volume(height: float | int, base_length: float | int) -> float:
    """
        Calculates the volume of a square pyramid from the given height and base length
        
        Args:
            height(float | int): the height of the sqare pyramid
            base_length(float | int): the length of a side of the square base
        
        Returns:
            volume(float): the volume of the square pyramid   
    """
    area_base: float = base_length ** 2
    volume: float = area_base * height / 3
    return volume


C1: float = -42.379
C2: float = 2.04901523
C3: float = 10.14333127
C4: float = -0.22475541
C5: float = -6.83783 * 10 ** -3
C6: float = -5.481717 * 10 ** -2
C7: float = 1.22874 * 10 ** -3
C8: float = 8.5282 * 10 ** -4
C9: float = -1.99 * 10 ** -6

def heat_index(temp: float | int, humidity: float | int) -> float:
    """
        Calculates the heat index based of constants C1-C9 and the input temperature and humidity        
        Args:
            temp(float | int): tempreture measured in fahrenheit
            humidity(float | int): humidity in percentage, example 97 = 97%
        
        Returns:
            heat_index(float): the given heat index from the inputs  
    """
    heat_index: float = C1 + (C2 * temp) + (C3 * humidity) + (C4 * temp * humidity) + (C5 * temp ** 2) + (C6 * humidity ** 2) + (C7 * (temp ** 2) * humidity) + (C8 * temp * humidity ** 2) + (C9 * (temp ** 2) * (humidity ** 2))
    return heat_index
    

def round_to_two(num: float) -> float:
    """
        Rounds any decimal number to two decimal places      

        Args:
            num(float): the number that will be rounded to two decimal places

        Returns:
            final_num(float): the 2 decimal rounded version of the input num
    """
    num_times_100: float = num * 100
    final_num: float = num_times_100 + 0.5
    final_num = final_num // 1
    final_num /= 100
    return final_num

def get_apparent_temperature(temp: float | int, humidity: float | int) -> float:
    """
        Calculates and displays the apparent temperature in fahrenheit based on the temperature and humidity in percentage      
        
        Args:
            temp(float | int): the temperature measured in fahrenheit
            humidity(floa | int): humidity measured in percentage, example 95 = 95% humidity
        
        Displays:
            "x F and y % humidity feels like z F, where x is the rounded temperature, y is the rounded humidity, and z is the rounded apparent temperature"

        Returns:
            apparent_temperature(float): the apparent temperature in fahrenheit
    """
    temp_rounded: float = round_to_two(temp)
    humidity_rounded: float = round_to_two(humidity)
    apparent_temperature: float = heat_index(temp, humidity)
    apparent_temperature_rounded: float = round_to_two(apparent_temperature)
    print(temp_rounded, "F and", humidity_rounded, "% humidity feels like", apparent_temperature_rounded, "F")
    return apparent_temperature
    

################################################################################

def main():
    #-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)

    print("Testing math_func_1()")
    ouput = math_func_1(0)
    print(ouput)
    output = math_func_1(1)
    print(output)
    output = math_func_1(3)
    print(output)


    print("Testing math_func_2()")
    output = math_func_2(1, 1, 1)
    print(output)
    output = math_func_2(2, 2, 3)
    print(output)
    output = math_func_2(5, 1, 3)
    print(output)


    print("Testing m_to_arshins()")
    output = m_to_arshins(3)
    print(output)
    output = m_to_arshins(6)
    print(output)
    output = m_to_arshins(0)
    print(output)
    output = m_to_arshins(1)
    print(output)
    output = m_to_arshins(20)
    print(output)


    print("Testing convert_min()")
    output = convert_min(129)
    print(output)
    output = convert_min(36548765)
    print(output)
    output = convert_min(12345678)
    print(output)
    output = convert_min(52123)
    print(output)
    output = convert_min(431415)
    print(output)
    

    print("Testing calc_final_price()")
    output = calc_final_price(35, 8)
    print(output)
    output = calc_final_price(150, 0)
    print(output)
    output = calc_final_price(58.69, 6)
    print(output)
    output = calc_final_price(144, 10)
    print(output)
    output = calc_final_price(1500, 50)
    print(output)
    output = calc_final_price(25, 100)
    print(output)


    print("Testing get_displacement()")
    output = get_displacement(3, 4, 5) 
    print(output)
    output = get_displacement(25, 3, 4) 
    print(output)
    output = get_displacement(35.5, 3.5, 7) 
    print(output)
    output = get_displacement(1, 1, 1) 
    print(output)
    output = get_displacement(9.8, 2.2, 5.1) 
    print(output)
    output = get_displacement(-9.8, -2.2, 5.1) 
    print(output)


    print("Testing p_volume()")
    output = p_volume(12, 6)
    print(output)
    output = p_volume(15, 6.5)
    print(output)
    output = p_volume(45.5, 2.75)
    print(output)
    output = p_volume(1,1)
    print(output)
    output = p_volume(2,2)
    print(output)
    output = p_volume(3,3)
    print(output)


    print("Testing heat_index()")
    output = heat_index(97.5, 46)
    print(output)
    output = heat_index(80, 97.3)
    print(output)
    output = heat_index(32, 0)
    print(output)
    output = heat_index(63, 43)
    print(output)
    output = heat_index(11, 50)
    print(output)


    print("Testing round_to_two()")
    output = round_to_two(85.6397)
    print(output)
    output = round_to_two(98.75)
    print(output)
    output = round_to_two(8.1)
    print(output)
    output = round_to_two(24.4532)
    print(output)
    output = round_to_two(74.631)
    print(output)
    output = round_to_two(873.689)
    print(output)


    print("Testing get_apparent_temperature()")
    output = get_apparent_temperature(85.6397, 80.7306) 
    print(output)
    output = get_apparent_temperature(76, 98.75) 
    print(output)
    output = get_apparent_temperature(85.6397, 80.7306) 
    print(output)
    output = get_apparent_temperature(83, 48) 
    print(output)
    output = get_apparent_temperature(83, 90) 
    print(output)
    output = get_apparent_temperature(75.99654, 99.999) 
    print(output)


if __name__ == "__main__":
    main()
