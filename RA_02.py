# File: RA_02.py         
# Author:  Deep Patel    
# Section: 003R
# E-mail:  djp6412@psu.edu    


## Required Functions

def get_code(num: int):
    if (num % 2 == 1 or ((num % 2 == 0) and (6 <= num <= 20))):
        return "CMPSC"
    elif ((num % 2 == 0 and 2<= num <= 5) or (num % 2 == 0 and num > 20)):
        return 131
    

def joint(num1: int, num2: int, num3: int) -> int:
    if (num1 + num2) % 2 == 0:
        if ((num1 + num2) % 7) % 2 == 1:
            return 1
        else:
            return 2
    elif (num1 + num2 + num3) % 2 == 1:
        divided = num1 * num2 * num3 / 11
        if (num1 * num2 * num3 % 11) % 2 == 0:
            return 3
        elif ((num1 * num2 * num3) // 10) > 10:
            return 4
        else:
            return 5
    else:
        return 6
        


## Optional Functions

def reverse(num: int) -> int:
    thousands_place_1digit = num // 1000
    num = num % 1000
    hundreds_place_2digit = (num // 100) * 10
    num = num % 100
    tens_place_3digit = (num // 10) * 100
    ones_place_4digit = (num % 10) * 1000
    return (ones_place_4digit + tens_place_3digit + hundreds_place_2digit + thousands_place_1digit)

    
