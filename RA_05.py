# File: RA_05.py         
# Author:  Deep Patel    
# Section: 003R
# E-mail:  djp6412@psu.edu    

def is_palindrome(lst: list) -> bool:
    small_item = 0
    big_item = len(lst)-1
    while small_item < big_item:
        if lst[small_item] == lst[big_item]:
            small_item +=1 
            big_item -= 1
        else:
            return False
    return True


def multiply(lst1: list, lst2: list) -> list:
    final_length = len(lst1)-1 + len(lst2)-1 + 1
    final_lst = [0] * final_length
    
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            final_lst[i+j] += lst1[i] * lst2[j]

    return final_lst
