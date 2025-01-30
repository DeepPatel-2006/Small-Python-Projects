# File: RA_06.py         
# Author:  Deep Patel 
# Section: 003R
# E-mail:  djp6412@psu.edu    

def translate(d: dict, msg: str) -> str:
    final_msg = []
    word_list = msg.split()
    for item in word_list:
        if item in d:

            final_msg.append(d[item])
        else:
            final_msg.append(item)

    return " ".join(final_msg)


print(translate({'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left', '1': 'one'}, 'up down left right forward 1 time'))


def get_pair_sum(lst: list, target: int) -> tuple | int:
    dict = {}
    for item in lst:
        dict[item] = target - item

    for item in dict:
        if dict[item] in dict:
            return (item, dict[item])
        
    return -1
        
