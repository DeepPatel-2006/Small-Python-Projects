"""
Course  : CMPSC 131, Fall 2024
File    : PS7.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006


Collaboration Statement: I worked with Soham on the last function to share ideas
"""

#-YOUR CODE STARTS HERE  (TODO) 


def skipping(num: int) -> int:

    """
        Returns the sum of 0 to every other integer upto the given integer

        Parameters:
            num (int): The top most integer

        Returns:
            int: The sum of every other integer from the input down to zero
    """

    if num <=0:
        return 0

    return num + skipping(num - 2)



def zig_zag(num: int) -> str:
    """
        Generates a zig-zag pattern of stars in a symetrical string format top to fown

        Parameters:
            num (int): The given amount number of stars in the first and last row

        Returns:
            str: a zig-zag pattern of stars in a symetrical string format top to fown
    """

    if num <= 0:
        return ''
    
    line = '*' * num  + "\n"

    return line + zig_zag(num-1) + line



def product_of_digits(num: int) -> int:
    """
        Computes the product of all non-zero digits of a number

        Parameters:
            num (int): The given number

        Returns:
            int: The product of all non-zero digits of the given number
    """

    if num == 0:
        return 1
    
    digit = num % 10

    if digit == 0:
        return 1 * product_of_digits(num // 10)

    return digit * product_of_digits(num // 10)



def near_by_unique(num: int) -> int:
    """
        Removes adjacent digits of the same value from the given integer

        Parameters:
            num (int): The given integer

        Returns:
            int: the transformed version if the integer without adjacent identitical digits
    """

    if num < 10:
        return num

    last_digit = num % 10
    second_last_digit = (num // 10) % 10

    if last_digit == second_last_digit:
        return near_by_unique(num // 10)
    else:
        return near_by_unique(num // 10) * 10 + last_digit  



def combine_lists(lst1: list, lst2, operation) -> list:
    """
        Combines two lists of numbers using a specified  operation

        Parameters:
            lst1 (list): The first list of numbers.
            lst2 (list): The second list of numbers.
            operation (str): The mathematical operation ('+', '-', '*', '/') to apply

        Returns:
            list: A new list with the results of applying the operation to corresponding elements of both lists
    """

    if  lst1 == []:
        return []
    
    if operation == '+':
        calculation = lst1[0] + lst2[0]
    elif operation == '-':
        calculation = lst1[0] - lst2[0]
    elif operation == '*':
        calculation = lst1[0] * lst2[0]
    elif operation == '/':
        calculation = lst1[0] / lst2[0]
    
    return [calculation] + combine_lists(lst1[1:], lst2[1:], operation)



def to_evens(lst: list) -> list:
    """
        Converts all odd numbers in a list to even numbers by adding one to the odd numbers

        Parameters:
            lst (list): The given list of numbers
        Returns:
            list: A new list where all odd numbers are added to 1
    """

    if lst == []:
        return []

    num = lst[0]
    if num %2 == 0:
        return [num] + to_evens(lst[1:])
    else:
        return [num + 1] + to_evens(lst[1:])



def to_evens_destructive_helper(lst, index):
    """
        Helper function to convert all odd numbers in a list to even numbers by adding them by 1. This function
        is used recursively and destructively modifies the original list

        Parameters:
            lst (list): The given list of numbers
            index (int): The current index to process
    """

    if index == len(lst) -1:
            
        if lst[-1] %2 != 0:
            lst[-1] += 1

        return lst

    if lst[index] % 2 != 0:
        lst[index] += 1
    to_evens_destructive_helper(lst, index + 1)
    
     

def to_evens_destructive(lst):
    """
        Converts all odd numbers in a list to even numbers by incrementing them by 1. This function
        destructively modifies the original list.

        Parameters:
            st (list): The input list of numbers
    """

    to_evens_destructive_helper(lst, 0)

    


def right_cumulative_gcd_helper(num1, num2):
    """
        finds the greatest common divisor (GCD) of two numbers using recursion

        Parameters:
            num1 (int): The first number
            num2 (int): The second number

        Returns:
            int: The GCD of the two numbers
    """

    if num2 == 0:
        return num1

    return right_cumulative_gcd_helper(num2, num1 % num2)



def right_cumulative_gcd(lst) -> list:
    """
        Computes the right cumulative GCD of a list of positive numbers. Each element in the new list 
        is the GCD of itself and all elements to its right

        Parameters:
            lst (list): The input list of positive numbers

        Returns:
            list: A new list where each element is replaced by the GCD of itself and all elements to its right
    """

    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return lst
    
    gcd_to_the_right = right_cumulative_gcd(lst[1:])
    gcd_compare = right_cumulative_gcd_helper(lst[0], gcd_to_the_right[0])

    return [gcd_compare] + gcd_to_the_right
    


def main():
    #-YOUR ASSERTIONS TO TEST FOR YOUR FUNCTIONS STARTS HERE (TODO)
    assert skipping(11) == 36
    assert skipping(10) == 30
    assert skipping(0) == 0


    assert zig_zag(3) == "***\n**\n*\n*\n**\n***\n"
    assert zig_zag(1) == "*\n*\n"
    assert zig_zag(0) == ""

    assert product_of_digits(1024) == 8
    assert product_of_digits(123) == 6
    assert product_of_digits(0) == 1

    assert near_by_unique(22224666666782) == 246782
    assert near_by_unique(111223) == 123
    assert near_by_unique(0) == 0

    assert combine_lists([10, 20, 30], [1, 2, 3], '*') == [10, 40, 90]
    assert combine_lists([10, 20, 30], [1, 2, 3], '+') == [11, 22, 33]
    assert combine_lists([10, 20, 30], [1, 2, 3], '-') == [9, 18, 27]

    assert to_evens([-5, 10, 19, 26, 8, 7]) == [-4, 10, 20, 26, 8, 8]
    assert to_evens([1, 3, 5]) == [2, 4, 6]
    assert to_evens([2, 4, 6]) == [2, 4, 6]                       

    lst1 = [-5, 10, 19, 26, 8, 7]
    to_evens_destructive(lst1)
    assert lst1 == [-4, 10, 20, 26, 8, 8] 

    lst2 = [1, 3, 5]
    to_evens_destructive(lst2)
    assert lst2 == [2, 4, 6]    

    lst3 = [2, 4, 6]
    to_evens_destructive(lst3)
    assert lst3 == [2, 4, 6]     
    
    
    assert right_cumulative_gcd_helper(13, 17) == 1  
    assert right_cumulative_gcd_helper(25, 25) == 25  
    assert right_cumulative_gcd_helper(0, 20) == 20 

    assert right_cumulative_gcd([20, 50, 15, 40, 10]) == [5, 5, 5, 10, 10]  
    assert right_cumulative_gcd([8, 12, 24]) == [4, 12, 24] 
    assert right_cumulative_gcd([7]) == [7]   









if __name__ == "__main__":
    main()