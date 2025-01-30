# File: RA_03.py         
# Author:  Deep Patel    
# Section: 003R
# E-mail:  djp6412@psu.edu 

def get_sum_for() -> float:
    total = 0
    for num in range(1, 101, 1):
        fraction = 1 / (num)
        total += fraction
    return total

def get_sum_while() -> float:
    num = 1
    total = 0
    while num <=100:
        fraction = 1 / (num)
        total += fraction
        num += 1
    return total

print(get_sum_for())
print(get_sum_while())


def sum_multiples_xor(num: int) -> int:
    if num <= 0:
        print("Input must be positive")
        return -1
    else:
        total = 0
        count = 0

        for i in range(1, num):
            mul_of_3 = i % 3 == 0
            mul_of_7 = i % 7 ==0

            if (mul_of_3 != mul_of_7):
                total += i
                count += 1
            
        print("Count of numbers summed:", count)

        return total
def get_index(num, digit) -> int:
    found = False
    location = 1
    while found == False:
        integer = num % 10
        if(integer == digit):
            return location
        num = num // 10
        location += 1
        if(num == 0):
            return -1
        

        
print(get_index(1213, 0))
