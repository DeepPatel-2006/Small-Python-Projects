"""
Course  : CMPSC 131, Fall 2024
File    : PS3.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006

Collaboration Statement: Sobay Vansao and Me Assisted eachother with logical thinking of functions
"""

#-YOUR CODE STARTS HERE  (TODO) 

def primes_count(num1: int, num2: int) -> int:
    """
        Displays all prime number within a range (inclusive)    

        Args:
            num1 (int): the beggining of the range
            num2 (int): the end of the range
        
        Displays:
            all prime numbers withing the interval
        
        Returns:
            the amount of prime numbers in the interval
    """
    total_count = 0

    if(num1>num2):
         print("ERROR")
         return -1
    
    for num in range(num1, num2 + 1):
        count = 0
        
         
        for number in range(1, num+1):
            if num % number == 0:
                count +=1

        if count == 2:
                print(num)
                total_count +=1

    return (total_count)


def decay(amount: int, years: int)-> float:
     """
        Calculates the the amount of radioactive cobalt-60 left after a given amount of years
        
        Args:
            amount (int): the oiginal amount of radioactive cobalt-60
            years (int): the amount of years the cobalt has decayed
        
        Returns:
            the amount oof radioactive cobalt-60 remaining after a given amount of years
    """
     remaining_amount = amount
     for year in range(1, years+1):
        remaining_amount = remaining_amount * (0.88)

     remaining_amount *= 100
     remaining_amount += 0.5
     remaining_amount //= 1
     remaining_amount /= 100
     return remaining_amount

print(decay(70, 3))


def fib_nums(n: int) -> None:
    """
        Displays the fibonacci sequence upto the nth term
        
        Args:
            n (int): the nth amount that the sequence will go upto
        
        Displays:
            the fibonacci sequence upto the nth term
    """
    num1 = 1
    num2 = 1
    placeholder = 0
    for num in range(1, n+1):        
        if num == 1:
            print('1')
        elif num == 2:
            print('1')
        else:
            print(num1 + num2)
            placeholder = num2 
            num2 = num2 + num1
            num1 = placeholder
                

def divisors_count(num: int) -> int:
    """
        Calculates the amount of divisors the given number has between 1 and upto the number itself
        
        Args:
            num (int): the number that will be checked for the amount of divisors it has less than itself
            
        Returns:
            the amount of divisors the given number has between 1 and upto the number itself
    """
    amount = 0
    value = 1
    while value <= num:
        if num % value == 0:
            amount += 1
        value += 1
    return amount

def count_digits(num: int) -> int:
    """
        Calculates the amount of digits a number has
        
        Args:
            num (int): the given number that will be checked for how many digits it has
            
        Returns:
            the amount of digit the given number has
    """
    digit = 0
    if num <0:
        num = num * -1

    while num != 0:
        num //= 10
        digit += 1
    return digit

def divisible_by(num: int, divisor: int) -> int:
    """
        Calculates and displays all positive integers less than or equal to the first number that are 
        divisible by the second number from smallest to largest before returning how many numbers were printed/
        
        Args:
            num (int): the number that represents the range [0, num] that will be checked numbers divisible by the divisor
            divisor (int): the number that the numbers in the range [0, num] will be divided by
        
        Displays:
            All integers in the range [0, num] that are divisible by the divisor
            
        Returns:
            the amount of divisors the given number has between 1 and upto the number itself
    """
    current_num = 1
    amount = 0
    while current_num <= num:

        if current_num % divisor == 0:
            print(current_num)
            amount += 1

        current_num += 1

    return amount


def is_armstrong_number(num: int) -> bool:
    """
        Checks wether or not a given number is an armtrong number
        
        Args:
            num (int): the given number that will be checked wether or not it is an armstrong number
            
        Returns (bool): 
            wether or not the given number is an armstrong number
    """
    final_num = num
    number_to_test = num
    total_digits = 0
    current_digit = 0
    sum = 0
    while num != 0:
        num = num // 10
        total_digits += 1

    while number_to_test != 0:
        current_digit = number_to_test % 10
        sum += current_digit ** total_digits
        number_to_test = number_to_test // 10

    if sum == final_num:
        return True
    else:
        return False
    
def factorial_sum(num: int) -> int:
    """
        Calculates the sum of all the integers from the range [1, num]
        
        Args:
            num (int): the number that the factorials will be summed up to
        
        Returns (int):
            the sum of all the integers from the range [1, num]
    """
    factorial_sum = 0
    for number in range (1, num + 1):
        factorial = 1
        for integer in range(1, number+1):
            
            factorial *= integer
        factorial_sum += factorial
    return factorial_sum

def is_perfect_number(num: int) -> bool:
    """
        Checks if the given number is a perfect number

        Args:
            num (int): the number that will be checked for its' status of being a perfect number
            
        Returns (bool):
            the status of the given number being a perfect number
    """
    sum_of_multiples = 0
    second_number = 0
    for number in range(1, int(num * 0.5) + 1):
        
        if num % number == 0:
            sum_of_multiples += number


    if sum_of_multiples == num:
        return True
    else:
        return False

def temp_sum(start: int, end: int) -> float:
    """
        Calculates the sum of the equivilant fahrenheit temperature for the celsius temperatures from start
        to end (inclusive) in increments of 5 degrees
        
        Args:
            start (int): the start of the temperature interval in celsius
            end (int): the end of the temperature interval in celsius
        
        Returns:
            the sum of the equivilant fahrenheit temperature for the censius temperatures from start to end
            in increments of 5 degrees
    """
    total = 0

    for temp_celsius in range(start, end+1, 5):
        fahrenheit = (temp_celsius * 9 / 5) + 32
        total = total + fahrenheit

    return total

def estimate(population: int | float) -> int:
    """
        Estimates the year in which the given population will be reached 
        
        Args:
            population (int | float): the population that will be used to estimate the year that will have the given population
        
        
        Returns (int):
            the year that will contain the population
    """
    current_population = 7
    years = 0

    while current_population < population:
        years += 1
        current_population *= 1.011

    return years + 2011

def classify(num: int) -> None:
    """
        Checks wether a number is deficient, abundant, or perfect

        Args:
            num (int): the number that sets the interval [2, num] for all integers that 
            will be checked for its deficient, abundant, or perfect status 
            
        Displays:
            all integers and their deficient, abundant, or perfect status within the range [2, num]
    """
    for value in range(2, num + 1):
        factors = 0
        for number in range(1, value):
            if value % number == 0:
                factors += number

        if factors == value:
            print(value, "is perfect")
        elif factors < value:
            print(value, "is deficient")
        else:
            print(value, "is abundant")


################################################################################

def main():
    #-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print("Testing primes_count()")
    print(primes_count(1, 6))
    print(primes_count(7, 25))
    print(primes_count(39, 4))
    print(primes_count(5, 15))
    print(primes_count(1, 1))
    print(primes_count(2, 2))

    print("Testing decay()")
    print(decay(10, 5))
    print(decay(70, 3))
    print(decay(806, 25))
    print(decay(211, 0))
    print(decay(21, 2))
    print(decay(24, 999))

    print("Testing fib_nums()")
    fib_nums(5)
    fib_nums(8)
    fib_nums(0)
    fib_nums(1)
    fib_nums(20)

    print("Testing divisors_count()")
    print(divisors_count(89))
    print(divisors_count(52))
    print(divisors_count(1))
    print(divisors_count(9))
    print(divisors_count(0))
    
    print("Testing count_digits()")
    print(count_digits(6589))
    print(count_digits(-6589))
    print(count_digits(123456788))
    print(count_digits(112233))
    print(count_digits(0))
    print(count_digits(232))

    print("Testing divisible_by()")
    print(divisible_by(10, 2))
    print(divisible_by(3, 1))
    print(divisible_by(1, 1))
    print(divisible_by(5, 2))
    print(divisible_by(9, 1))

    print("Testing is_armstrong_number()")
    print(is_armstrong_number(153))
    print(is_armstrong_number(169))
    print(is_armstrong_number(2342))
    print(is_armstrong_number(654463))
    print(is_armstrong_number(999))
    
    print("Testing factorial_sum()")
    print(factorial_sum(5))
    print(factorial_sum(12))
    print(factorial_sum(1))
    print(factorial_sum(2))
    print(factorial_sum(3))

    print("Testing temp_sum()")
    print(temp_sum(10, 30))
    print(temp_sum(50, 3000))
    print(temp_sum(12, 73))
    print(temp_sum(1, -2))
    print(temp_sum(3, 4))
    print(temp_sum(5, 15))

    print("Testing estimate()")
    print(estimate(8))
    print(estimate(10))
    print(estimate(11.5))
    print(estimate(200))
    print(estimate(1))
    print(estimate(23))

    print("Testing classify()")
    classify(25)
    classify(2)
    classify(1)
    classify(10)




    pass

if __name__ == "__main__":
    main()
