"""
Course  : CMPSC 131, Fall 2024
File    : PS2.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006

Collaboration Statement: YOUR_STATEMENT_HERE
"""

#-YOUR CODE STARTS HERE  (TODO) 


def is_odd(num: int) -> bool:
    if (num % 2 == 1):
        return True
    else: 
        return False
    
def temperature_conversion(temp: float | int, to_f: bool) -> float:
    if to_f == True:
        return (9 * temp / 5) + 32
    else:
        return (temp - 32) * 5 / 9
    
def cascade(x: int, y: int, z: int) -> float:
    if z % 7 == 0:
        return x * y
    elif x <= (y-z) and x != 0:
        return (y - (2 * z)) / x
    else:
        return x - z
    


    
def get_bill(num_bagels: int) -> float:
    """
        Calculates the total cost of the order of bagels
        
        Args:
            num_bagels (int): the number of bagels in the order
            
        Returns:
            Returns the price of the order (float)
    """
    if type(num_bagels) != int:
        return -1
    elif 0 < num_bagels < 6:
        return num_bagels * 0.85
    elif num_bagels >= 6:
        return num_bagels * 0.55
    else:
        return -1
    

def get_letter_grade(grade: int | float) -> str:
    """
        Calculates the letter grade from the percentage grade
        
        Args:
            grade (int | float): the percentage grade of the student
            
        Returns:
            Returns the letter grade of the student (string)
    """
    if grade >= 93.0:
        return 'A'
    elif grade >= 90.0:
        return 'A-'
    elif grade >= 87.0:
        return 'B+'
    elif grade >= 83.0:
        return 'B'
    elif grade >= 80.0:
        return 'B-'
    elif grade >= 77.0:
        return 'C+'
    elif grade >= 70.0:
        return 'C'
    elif grade >=60.0:
        return 'D'
    else:
        return 'F'


def intersect(x1: int | float, y1: int | float, radius1: int | float, x2: int | float, y2: int | float, radius2: int | float) ->  bool:
    """
        Calculates wether two circles intersect eachother or not
        
        Args:
            x1 (int | float): x coordinate value of the center of the first circle

            y1 (int | float): y coordinate value of the center of the first circle

            radius1 ( int | float): the length of the radius of the first circle

            x2 (int | float): x coordinate value of the center of the first circle

            y2 (int | float): y coordinate value of the center of the first circle

            radius2 ( int | float): the length of the radius of the first circle

        Returns:
            Returns wether of not the circles intersect (boolean)
    """
    distance_between_center = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5
    sum_radius = radius1 + radius2
    if distance_between_center == 0 and radius1 != radius2:
        return False
    elif distance_between_center > sum_radius:
        return False
    else:
        return True

def get_num(num : float | int, bound1: float | int, bound2: float | int) -> float | int:
    """
        Finds the number that is in between of the other two numbers
        
        Args:
            num (int | float): the first number
            bound1 (int | float): the upper bound
            bound2 (int | float): the lower bound
            
        Returns:
            Returns the number that is in between the other two numbers (float)
    """
    
    if bound1 <= bound2:
        lower_bound = bound1
        upper_bound = bound2
    elif bound2 < bound1:
        lower_bound = bound2
        upper_bound = bound1
    if lower_bound <= num <= upper_bound:
        return num
    elif num > upper_bound:
        return upper_bound
    else:
        return lower_bound
    
def how_many(eggs: int) -> int:
    """
        Calculates the smallest number of cartons needed to contain the given amount of eggs
        
        Args:
            eggs (int): the number of eggs that need to be contained
            
        Returns:
            Returns the smallest number of cartoons required to hold the provided number of eggs
    """
    if eggs % 12 == 0:
        cartons = eggs // 12
    else:
        cartons = (eggs // 12) + 1
    return cartons

def is_even_positive(num: int | float) -> bool:
    """
        Calculates wether the given number is an integer, positive, and even
        
        Args:
            num (int | float): the given number to be tested
            
        Returns:
            Returns wether or not the provided number is an integer, positive, and even (boolean)
    """
    if(type(num) == int) and num % 2 == 0 and num > 0:
        return True
    else:
        return False
    
def is_triangle(side1: int | float, side2: int | float, side3: int | float) -> bool:
    """
        Calculates wether the 3 given side lengths of a triangle can make a real triangle
        
        Args:
            side1 (int | float): the first side of the triangle
            side2 (int | float): the second side of the triangle
            side3 (int | float): the third side of the triangle
        Returns:
            Returns wether or not the three sides can formulate a real triange (boolean)
    """
    if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
        return True
    else:
        return False
    
def get_chinese_zodiac(year: int) -> str:
    """
        Calculates the zodiac sign of a person based on their birth year
        
        Args:
            year (int): the year that a person is born
        Returns:
            Returns the zodiac sign on the person
    """
    
    if (year % 12 == 0):
        return 'monkey'
    elif (year % 12 == 1):
        return 'rooster'
    elif (year % 12 == 2):
        return 'dog'
    elif (year % 12 == 3):
        return 'pig'
    elif (year % 12 == 4):
        return 'rat'
    elif (year % 12 == 5):
        return 'ox'
    elif (year % 12 == 6):
        return 'tiger'
    elif (year % 12 == 7):
        return 'rabbit'
    elif (year % 12 == 8):
        return 'dragon'
    elif (year % 12 == 9):
        return 'snake'
    elif (year % 12 == 10):
        return 'horse'
    else:
        return 'sheep'


def get_maximum(num1: int , num2: int) -> int:
    """
        Finds which of the two numbers is bigger
        
        Args:
            num1 (int): the first number
            num2 (int): the second number

        Returns:
            Returns the bigger number (int)
    """
    if num1 >= num2:
        return num1
    else: 
        return num2
def get_maximum_below(num1: int, num2: int, limit: int) -> int:
    """
        Calculates the biggest number below a limit
        
        Args:
            num1 (int): the first number
            num2 (int): the second number
            limit (int): the limit value
        Returns:
            Returns the biggest number below the limit (int)
    """
    if (num1 >= limit):
        return num2
    if (num2 >= limit):
        return num1
    else:
        return get_maximum(num1, num2)
    
def get_the_best(num1: int, num2: int, num3: int, num4: int, num5: int) -> int:
    """
        Calculates the median of a group of 5 numbers
        
        Args:
            num1 (int): the first number
            num2 (int): the second number
            num3 (int): the third number
            num4 (int): the fourth number
            num5 (int): the fifth number

        Returns:
            Returns the median (int)
    """
    first_max = get_maximum(num1, num2)
    second_max = get_maximum(first_max, num3)
    third_max = get_maximum(second_max, num4)
    final_max = get_maximum(third_max, num5)

    second_biggest_1 = get_maximum_below(num1, num2, final_max)
    second_biggest_2 = get_maximum_below(num3, num4, final_max)
    second_biggest_3 = get_maximum_below(num4, num5, final_max)


    final_second_biggest_1 = get_maximum(second_biggest_1, second_biggest_2)
    final_second_biggest_2 = get_maximum(second_biggest_2, second_biggest_3)
    final_second_biggest_final = get_maximum(final_second_biggest_1, final_second_biggest_2)

    third_biggest = get_maximum_below(num1, num2, final_second_biggest_final)
    third_biggest = get_maximum_below(num3, third_biggest, final_second_biggest_final)
    third_biggest = get_maximum_below(num4, third_biggest, final_second_biggest_final)
    third_biggest = get_maximum_below(num5, third_biggest, final_second_biggest_final)

    return third_biggest



################################################################################

def main():
#-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)

    print("Testing is_odd")
    print(is_odd(3))
    print(is_odd(3232432))
    print(is_odd(134))
    print(is_odd(63076))
    print(is_odd(6970))


    print("Testing temperature_conversion")
    print(temperature_conversion(32, True))
    print(temperature_conversion(320, False))
    print(temperature_conversion(2, True))
    print(temperature_conversion(1, False))
    print(temperature_conversion(48398, True))


    print("Testing cascade")
    print(cascade(1, 1, 1))
    print(cascade(13, 11, 41))
    print(cascade(312, 82, 19))
    print(cascade(8, 6, 4))
    print(cascade(876, 37377, 3783))


    print("Testing get_bill")
    print(get_bill(12))
    print(get_bill(8))
    print(get_bill(2))
    print(get_bill(-7))
    print(get_bill(78.0))
    print(get_bill(2226))
    print(get_bill(-724))
    print(get_bill('89'))


    print("Testing get_letter_grade")
    print(get_letter_grade(100))
    print(get_letter_grade(92.99))
    print(get_letter_grade(81.5))
    print(get_letter_grade(73.8))
    print(get_letter_grade(3))
    print(get_letter_grade(313.21))
    print(get_letter_grade(54))
    print(get_letter_grade(191.300))


    print("Testing intersect")
    print(intersect(2, 3, 12, 15, 28, 10))
    print(intersect(3, 4, 5, 14, 18, 8))
    print(intersect(1.0, 1, 3, 5, 4.0, 2))
    print(intersect(242, 374, 192, 615, 328, 120))
    print(intersect(0, 0, 12, 3, 1, 53))
    print(intersect(2, 3, 12, 2, 3, 1))


    print("Testing get_num")
    print(get_num(1, 3, 5))
    print(get_num(4.7, 3, 5))
    print(get_num(6, 5, 3))
    print(get_num(1, 1, 1))
    print(get_num(5, 6, 13))
    print(get_num(36, 5524 ,52242))


    print("Testing how_many")
    print(how_many(5))
    print(how_many(24))
    print(how_many(6548))
    print(how_many(541))
    print(how_many(9694))
    print(how_many(120000))


    print("Testing is_even_positive")
    print(is_even_positive(12))
    print(is_even_positive(12.0))
    print(is_even_positive("hello"))
    print(is_even_positive(33))
    print(is_even_positive(-12))
    print(is_even_positive(384))
    print(is_even_positive(-14))
    print(is_even_positive(True))


    print("Testing is_triangle")
    print(is_triangle(3, 4, 5))
    print(is_triangle(3, -4, 5))
    print(is_triangle(2.5, 3.75, 5.1))
    print(is_triangle(300, 400, 500))
    print(is_triangle(194, 194, 195))
    print(is_triangle(2, 2, 1))


    print("Testing get_chinese_zodiac")
    print(get_chinese_zodiac(2003))
    print(get_chinese_zodiac(2022))
    print(get_chinese_zodiac(2023))
    print(get_chinese_zodiac(2020))
    print(get_chinese_zodiac(2021))
    print(get_chinese_zodiac(2031))
    print(get_chinese_zodiac(1947))
    print(get_chinese_zodiac(20000003))
    print(get_chinese_zodiac(294))


    print("Testing get_maximum")
    print(get_maximum(5, 7))
    print(get_maximum(4, 2))
    print(get_maximum(1, 1))
    print(get_maximum(53144,18448))
    print(get_maximum(2307, 319))


    print("Testing get_maximum_below")
    print(get_maximum_below(4, 2, 12))
    print(get_maximum_below(4, 2, 1))
    print(get_maximum_below(1, 3, 5))
    print(get_maximum_below(6, 6, 6))
    print(get_maximum_below(6, 99999, 1))


    print("Testing get_the_best")
    print(get_the_best(6, 8, 10, 2, 4))
    print(get_the_best(32, 83, 772, 1000, 1983))
    print(get_the_best(6234, 8424, 1047, 2, 474))
    print(get_the_best(3, 4, 6, 000, 43))
    print(get_the_best(9, 9, 9, 9, 9))


    

if __name__ == "__main__":
    main()
