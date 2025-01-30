# File: RA_08.py         
# Author:  Deep Patel    
# Section: 003R
# E-mail:  djp6412@psu.edu


def awards(lst: list) -> dict:
    dict_final = {}
    for category, movie in lst:
        if movie not in dict_final:
            dict_final[movie] = 1
        else:
            dict_final[movie] += 1
    return dict_final



def get_largest(lst: list) -> int:
    max = lst[0][0]
    for item in lst:
        for number in item:
            if number > max:
                max = number

    return max


def get_row_average(lst: list) -> list:
    final_list = []
    for item in lst:
        total = 0
        length = 0
        for number in item:
            total += number
            length += 1

        average = total / length
        final_list.append(average)
    return final_list




