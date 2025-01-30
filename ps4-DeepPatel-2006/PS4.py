"""
Course  : CMPSC 131, Fall 2024
File    : PS4.py 
Name    : Deep Patel

GitHub User: DeepPatel-2006

Collaboration Statement: YOUR_STATEMENT_HERE
"""

#-YOUR CODE STARTS HERE  (TODO) 

def is_vowel(char: str) -> bool:

    """
        Checks if a character is a vowel

        Args:
            char (str): the char that will be checked for wether its a vowel or not

        Returns:
            (boolean): True if the character is vowel and False if the character is not a vowel
    """


    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
        return True
    else:
        return False


def count_vowels(txt: str) -> int:

    """
        Counts the amount of vowels in a string

        Args:
            txt (str): the input string that will be checked for how many vowels it contains

        Returns:
            count (int): the amount of vowels in the input string
    """

    count = 0

    for character in txt:

        if is_vowel(character):
            count +=1

    return  count


def hailstone(num: int) -> list:

    """
        Finds the hailstone sequence with the sequence starting at the given integer

        Args:
            num (int): the input number which is what the hailstone sequence will start with

        Returns:
            final_list (list): the hailstone sequence that starts with the input integer
    """

    final_list = []
    final_list.append(num)

    while num != 1:

        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1

        final_list.append(num)

    return final_list
        
def get_second(txt: str) -> str:

    """
        Finds the second word in a string that contains words seperated by commas

        Args:
            txt (str): the input string that has words seperated by commas

        Returns:
            second (str): the second word in the string
    """

    second: str
    txt_list = txt.split(",")
    second = txt_list[1].strip()

    return second

def find(char: str, txt: str, num: int) -> int:

    """
        Returns the index of the first occourrence of a character in a string starting from a given start point, or if no such occourrence is found or the given string txt is empty, the function returns -1

        Args:
            char (str): the character that will be searched for its first occourrence from a given starting point
            txt (str): the input string that will be checked
            num (int): the index that will be the start for the search of the first occourrence of char


        Returns:
            the index of the first occourrence of char from the starting point, or returns -1 if char is not found or the input string char is empty
    """
    while num <= len(txt) - 1:

        if txt[num] == char:
            return num
        else:
            num += 1

    return -1

def find_first_vowel(txt1: str) -> int:

    """
        Returns the idex of the first vowel found in the given string txt1 or returns the length of the given string txt1 if no such occourrence is found

        Args:
            txt1 (str): the given string that will be checked for its first vowel's index

        Returns:
            lowest (int): the idex of the first vowel found in the given string txt1 or returns the length of the given string txt1 if no such occourrence is found
    """
    
    final_list = []
    num1 = find('a', txt1, 0)
    num2 = find('e', txt1, 0)
    num3 = find('i', txt1, 0)
    num4 = find('o', txt1, 0)
    num5 = find('u', txt1, 0)
    num6 = find('y', txt1, 1)
    final_list.append(num1)
    final_list.append(num2)
    final_list.append(num3)
    final_list.append(num4)
    final_list.append(num5)
    final_list.append(num6)


    lowest = len(final_list)
    
    for i in range(0, len(final_list)):
        
        if final_list[i] >= 0 and final_list[i] <= lowest:
            lowest = final_list[i]
    
    if lowest == len(final_list):
        return len(txt1)
    else:
        return lowest


def get_pig_latin(text: str) -> str:

    """
        Converts the given string text into pig latin based on given rules

        Args:
            text (str): the given string that will be converted into pig latin

        Returns:
            final_txt (str): the pig latin version of the input string text
    """
    

    final_txt = ''
    if find_first_vowel(text) == 0:
        final_txt = text + 'hay'
    elif text[0] == 'q':
        final_txt = text[2:] + "quay"
    else:
        final_txt = text[find_first_vowel(text):] + text[0: find_first_vowel(text)] + "ay"


    return final_txt


def longest_word(sentence: str) -> str:

    """
        Finds the longest word in a string of words seperated by a space

        Args:
            sentence (str): the input string that will be checked for its longest word

        Returns:
            longest_word (str): the longest word in the input string sentence
    """

    txt_list = sentence.split()    

    longest_word = txt_list[0]

    for current_word in txt_list:
        if len(current_word) > len(longest_word):
            longest_word = current_word
    return longest_word



def replace_vowels_in_list(strings_list):

    """
        Replaces all the vowels in the words with the letter z in a list of string elements

        Args:
            strings_list (list): the input list with string elements

        Displays:
            strings_list (list): the original list that has all of its vowels replaced by the letter z

        Returns:
            None
    """

    word_index = 0
    for word in strings_list:
        letter_index = 0
        new_word = ""
        for letter in word:
            
            if is_vowel(letter):
                new_word += 'z'
            else:
                new_word += letter


            letter_index += 1
        strings_list[word_index] = new_word
        word_index += 1

    print(strings_list)



def alternating_sum(num_list: list) -> float:

    """
        Finds the alternating sum of the elements in a list

        Args:
            num_list (list): the input list with integer elements

        Returns:
            total (float): the alternating sum of the input list
    """
    total = 0.0
    for i in range(len(num_list)):
        
        if i % 2 == 0:
            total += num_list[i]
        else:
            total -= num_list[i]


    return total



def get_max(number_list: list) -> int:

    """
        Finds the maximum value in a given list

        Args:
            number_list (list): the input list with integer elements

        Returns:
            biggest (int): the biggest integer value in the input list
    """
    biggest = number_list[0]
    for item in number_list:

        if item > biggest:
            biggest = item


    return biggest


def max_in_window(num_list: list, window_length: int) ->list:

    """
        Finds a list that contains the maximum value of each of the sliding windows without destroying the original list

        Args:
            num_list (list): the input list of integer elements
            window_length (int): the length of each window

        Returns:
            final_list (list): a list with elements that are the maximum value in each window
    """
    final_list = []
    for i in range(len(num_list) - window_length +1):
        window = num_list[i: i+window_length]
        final_list.append(get_max(window))
    return final_list
################################################################################

def main():
    #-YOUR TESTS FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print("Testing count_vowels()")
    print(count_vowels("programming"))
    print(count_vowels("ApplE"))
    print(count_vowels("CMPsc131"))
    print(count_vowels("wrasr231d"))
    print(count_vowels("ooopout4"))


    print("Testing hailstone()")
    print(hailstone(5))
    print(hailstone(6))
    print(hailstone(16))
    print(hailstone(63))
    print(hailstone(11))


    print("Testing get_second()")
    print(get_second('mouse, cat, dog, pig, lion'))
    print(get_second('apple, wef h  , banana'))
    print(get_second('apple,qdqpear            , banana'))
    print(get_second('apple,           wrwr            , banana'))
    print(get_second('apple,           #Q$$!, banana'))


    print("Testing find()")
    print(find('p', 'hello', 0))
    print(find('e', 'hello', 2))
    print(find('e', 'hello', 0))
    print(find('l', 'hello', 1))
    print(find('l', 'hello', 3))
    print(find('g', 'angel', 4))
    print(find('s', 'apples', 1))
    print(find('t', 'titanicc', 5))


    print("Testing find_first_vowel()")
    print(find_first_vowel("hello"))
    print(find_first_vowel("drone"))
    print(find_first_vowel("r2d2"))
    print(find_first_vowel("yummy"))
    print(find_first_vowel("dry"))
    print(find_first_vowel("ortogonal"))
    print(find_first_vowel("reddiferr"))
    print(find_first_vowel("east"))
    print(find_first_vowel("common"))


    print("Testing get_pig_latin()")
    print(get_pig_latin('ortogonal'))
    print(get_pig_latin('quacking'))
    print(get_pig_latin('blue'))
    print(get_pig_latin('dry'))
    print(get_pig_latin('kmr'))
    print(get_pig_latin('fortune'))
    print(get_pig_latin('mystic'))
    print(get_pig_latin('charismatic'))



    print("Testing longest_word()")
    print(longest_word("I love programming in Python"))
    print(longest_word("The quick brown fox jumps over the lazy dog"))
    print(longest_word("I went to school then took a homework"))
    print(longest_word("The table ball towel in wallet"))
    print(longest_word("Pennsylvania keyboard spoon calculator"))





    print("Testing replace_vowels_in_list()")
    replace_vowels_in_list( ['hello', 'world'])
    replace_vowels_in_list( ['summation', 'would'])
    replace_vowels_in_list( ['thair', 'there', 'keyboard'])
    replace_vowels_in_list( ['hello', 'world', 'towel', 'titanic'])



    print("Testing alternating_sum()")
    print(alternating_sum([1, 5]))
    print(alternating_sum([1, 5, 17]))
    print(alternating_sum([1, 5, 17, 4]))
    print(alternating_sum([3, 65, 87, 32, 12]))
    print(alternating_sum([43, 67, 1, 323 ,2]))
    print(alternating_sum([0, 0, 0, 0, 0]))
    print(alternating_sum([3, 1, 9, 2, 5, 6, 2, 1, 5, 7, 9, 4, 2, 1, 5, 7, 8, 9, 9, 3]))



    print("Testing max_in_window")
    print(max_in_window([2, 5, 12, 3, 4], 2))
    print(max_in_window([1, 3, 5, 1, 2, 4, 7, 8], 4))
    print(max_in_window([1, 3, 0, 3, 5, 3, 6, 2, 8], 3))
    print(max_in_window([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
    print(max_in_window([1, 0, 9, 3, 6, 4 ,2 ,2, 4, 8], 6))
    print(max_in_window([9, 9, 0,5, 3, 1, 5, 7, 8, 2, 1, 3], 2))
if __name__ == "__main__":
    main()
