"""
Course  : CMPSC 131, Fall 2024
File    : PS5.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006

Collaboration Statement: YOUR_STATEMENT_HERE

Notice:
Revise the Grading notes posted in the Canvas Assignemnt
Grading Requirements for Code Documentation and testing have changed!
"""

#-YOUR CODE STARTS HERE  (TODO) 

def to_lowercase(txt: str) -> str:

    """
        Converts a given string into its lowercase version

        Args:
            txt (str): the string that will be converted into its lowercase version

        Returns:
            restult (str): the lowercase version of the given string
    """

    result = ''
    for char in txt:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result



def invert_dict(dict: dict) -> dict:

    """
        inverts a dictionary

        Args:
            dict (dict): the given dictionary that will be inverted

        Returns:
            new_dict (dict): the inverted version of the input dictionary
    """

    new_dict = {}

    for item in dict:
        value = dict[item]
        if (value in new_dict) == False:
            new_dict[value] = [item]
        else:
            new_dict[value].append(item)
    return new_dict



def char_frequency(txt: str) -> dict:
    
    """
        Returns a dictionary with its keys as letters and its values representing how many times those characters appear in a given string

        Args:
            txt (str): the given string that will be checked for its letter's frequency

        Returns:
            freq_dict (dict): the dictionary that represents the frequency of the input string's characters
    """

    freq_dict = {}
    for char in txt:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)

            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return freq_dict



def char_frequency_with_punctuation(txt: str) -> dict:

    """
        Returns a dictionary with its keys as letters and its values representing how many times those characters appear in a given string

        Args:
            txt (str): the given string that will be checked for its letter's frequency

        Returns:
            freq_dict (dict): the dictionary that represents the frequency of the input string's characters
    """

    freq_dict = {}
    for char in txt:
            
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + 32)

            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    
    
    return freq_dict



def frequency_difference(txt1: str, txt2: str) -> dict:

    """
        returns a dictionary containing characters that appear in the first string but not in the second, along with their frequencies

        Args:
            txt1 (str): the given string that will be checked for its letter's frequency
            txt2 (str): the given string that will be checked for its letter's frequency

        Returns:
            char_frequency_with_punctuation(difference_string) (dict): the dictionary that represents the frequency of the difference in the string's characters' frequencies
    """
    lower_txt1 = to_lowercase(txt1)
    lower_txt2 = to_lowercase(txt2)

    difference_string = ''
    for item in lower_txt1:
        if (item in lower_txt2) == False:
            difference_string += item
    return char_frequency_with_punctuation(difference_string)





def find_missing_pangram_chars(txt: str) -> list:

    """
        finds the missing characters required to make a string a panagram

        Args:
            txt (str): the given string that will be checked for its missing panagram letters

        Returns:
            final_list (list): the letters in the form of a list that are required to turn the given string into a panagram
    """


    final_list = []
    txt_lower = to_lowercase(txt)
    lower_all = 'abcdefghijklmnopqrstuvwxyz'
    for char in lower_all:
        if (char in txt_lower) == False:
            final_list.append(char)
    return final_list



def are_anagrams(txt1: str, txt2: str) -> bool:

    """
        checks if 2 strings are anagrams

        Args:
            txt1 (str): the input string that will be checked for if its an anagram with another string
            txt2 (str): the input string that will be checked for it its an anagram with another string

        Returns:
            (bool): True if the 2 strings are anagrams, and False if they are not)
    """

    
    if len(frequency_difference(txt1, txt2)) == 0:
        return True
    else: 
        return False




def find_anagrams(txt: str, list: list) -> list:

    """
        finds all the anagrams between a string and all the strings in the list

        Args:
            txt (str): the given string that will be checked for its anagrams with the elements of the input list
            list (list): the given list that will be checked for its anagrams with the input string

        Returns:
            final_list (list): a list with the elements of the input list that are anagrams with the input string
    """

    final_list = []
    for item in list:
        if are_anagrams(txt , item):
            final_list.append(item)
    return final_list




def find_anagram_pairs(lst: list) -> list:

    """
        finds the the index values of the anagrams in a given list

        Args:
            list (list): the given list which will be checked for its anagram values

        Returns:
            anagram_pairs (list): a list of tuple values that represent the index values of the anagrams in the input list
    """
    anagram_pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                anagram_pairs.append((i, j))
    return anagram_pairs
    


################################################################################

def main():
    #-YOUR ASSERTIONS TO TEST FOR YOUR FUNCTIONS STARTS HERE (TODO)
    print("Testing to_lowercase()")

    print(to_lowercase("OEFH"))
    print(to_lowercase("3rfFAEF"))
    print(to_lowercase("4t23yw!(FW)"))


    print("Testing invert_dict()")

    print(invert_dict({'a': 1, 'b': 2, 'c': 1, 'd': 2, 3.75: 7}))
    print(invert_dict({'c': 4, 'b': 99, 'g': 1, 'd': 2, 3.75: 7}))
    print(invert_dict({'32': 32, '0': 23, 'c': 32, 'c': 2, 3.75: 7}))
    print(invert_dict({'a': 11, 'b': 21, 'c': 1, 'd': 2, 3.75: 7}))


    print("Testing char_frequency()")

    print(char_frequency("~ABC abc!!!!!!! !!!!!!  "))
    print(char_frequency("WFIEHF)820rh82r879fg"))
    print(char_frequency("2wrh08csh"))
    print(char_frequency("fdwfjwpfjw"))



    print("Testing frequency_difference()")

    print(frequency_difference("abcd!!", "A~"))
    print(frequency_difference("abcdww!!", "A2rr2~"))
    print(frequency_difference("abcdfwffd!!", "fewA~"))
    print(frequency_difference("abrew3tcd!!", "A~ouijhyrtgef"))


    print("Testing  find_missing_pangram_chars()")

    print(find_missing_pangram_chars("The quick brown fox"))
    print(find_missing_pangram_chars("Dishwashed"))
    print(find_missing_pangram_chars("soap"))
    print(find_missing_pangram_chars("Follow me"))



    print("Testing are_anagrams()")

    print(are_anagrams("Listen", "Silent"))
    print(are_anagrams("Listen", "Google"))
    print(are_anagrams("titanic", "titanci"))
    print(are_anagrams("forum", "murof"))
    print(are_anagrams("fhits", "shifts"))


    print("Testing find_anagrams()")

    print(find_anagrams("listen", ["ENlist", "google", "inLets", "banana"]))
    print(find_anagrams("titanic", ["ENlist", "google", "citanai", "banana"]))
    print(find_anagrams("tacocat", ["ENlist", "google", "inLets", "tacoocat"]))
    print(find_anagrams("keyboard", ["key", "board", "boardkey", "city"]))



    print("Testing find_anagram_pairs()")
    print(find_anagram_pairs(["listen", "silent", "enlist", "inlets", "google"]))
    print(find_anagram_pairs(['a', 'b']))
    print(find_anagram_pairs(["ENlist", "google", "citanai", "banana"]))
    print(find_anagram_pairs(["ENlist", "google", "inLets", "tacoocat"]))
    print(find_anagram_pairs(["key", "board", "boardkey", "yek"]))



if __name__ == "__main__":
    main()
