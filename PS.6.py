"""
Course  : CMPSC 131, Fall 2024
File    : PS6.py 
Name    : Deep Patel

GitHub User:   DeepPatel-2006


Collaboration Statement: Somay Bansal: I worker beside him and shared some problem solving ideas to get us through the problem set
"""

#YOUR CODE STARTS HERE  (TODO)


def create_list(filename: str) -> list:

    """
        returns the 2d list verion of the file with numbers in it

        Args:
            filename (str): the file that will be converted into the 2d list

        Returns:
            final_list (list): the 2d list version of the input file
    """

    file = open(filename, 'r')
    everything = file.readlines()
    file.close
    final_list = []
    float_list = []
    for line in everything:
        float_list = []
        line = line.strip().split(',')
        for item in line:
            float_list.append(float(item))
        final_list.append(float_list)
    
    return final_list


def create_list_letter(filename: str):

    """
        returns the 2d list verion of the file with letters in it

        Args:
            filename (str): the file that will be converted into the 2d list

        Returns:
            final_list (list): the 2d list version of the input file with elements of the list being string values
    """

    file = open(filename, 'r')
    everything = file.readlines()
    file.close()
    final_list = []
    float_list = []
    for line in everything:
        float_list = []
        line = line.split()
        for item in line:
            float_list.append((item))
        final_list.append(float_list)
    
    return final_list

def sum_of_rows(filename: str) -> list:

    """
        returns a 2d list where each entry in the list represents the total of each row of the given file

        Args:
            filename (str): the file that will be checked for the sum of the values of its rows

        Returns:
            output_list (list): the 2d list that represents the sum values of the entries of rows of a given file
    """

    data = create_list(filename)
    total = 0
    output_list = []
    for row in data:
        total = 0
        for number in row:
            total += number
        output_list.append(round(total, 2))

    return output_list

def max_num_columns(list: list) -> int:

    """
        returns the max number of columns in the 2d list

        Args:
            list (list): the 2d list that will be checked for its maximum number of columns

        Returns:
            max (int): the maximum number of columns in the given list
    """
    count = 0
    max = 0
    for row in list:
        count = 0
        for number in row:
            count += 1
        if count > max:
            max = count
    return max


def sum_of_columns(filename: str) -> list:

    """
        returns a 2d list where each entry in the list represents the total of each column of the given file

        Args:
            filename (str): the file that will be checked for the sum of the values of its columns

        Returns:
            final_list (list): the 2d list that represents the sum values of the entries of columns of a given file
    """

    data = create_list(filename)
    total = 0
    max_columns = max_num_columns(data)

    final_list = max_columns * [0]

    for row in data:
        count = 0
        for num in row:
            final_list[count] += round(num, 2)
            count += 1

    return final_list


def min_max_per_row(filename: str):

    """
        returns a 2d list where each entry is a tuple in the list that represents minimum and maximum value in each row of the given file

        Args:
            filename (str): the file that will be checked its min and max values in each row

        Returns:
            final_list (list): list of tuples that represent the min and max values of each row of the given file
    """

    data = create_list(filename)
    final_list = []
    for row in data:
        min = row[0]
        max = row[0]
        for num in row:
            if num < min:
                min = num
            if num > max:
                max = num
        final_list.append((min, max))
    return final_list

    

def average_of_columns(filename: str):

    """
        returns a list where each entry in the list represents the average value of the columns inside the file

        Args:
            filename (str):the file that will be checked for its average column values

        Returns:
            final_average_list (list): the list that contains the average values of the columns of the given file
    """

    data = create_list(filename)
    total = 0
    max_columns = max_num_columns(data)

    final_list = max_columns * [0]
    count_list = max_columns * [0]
    final_average_list = []

    for row in data:
        count = 0
        for num in row:
            final_list[count] += num
            count_list[count] += 1
            count += 1

    for i in range(len(count_list)):
        val = final_list[i]
        length = count_list[i]
        final_average_list.append(round((val/length), 2))
    return final_average_list



def zero_below(list: list, min: int) -> None:

    """
        mutates a 2d list which will have values of 0 where the input list had values that were less than the given threshold value min

        Args:
            list (list): the list that will be checked for having values less that the given threshold value min
            min (int): the given threshold value

        Returns:
            None
    """

    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            if list[i][j] < min:
                list[i][j] = 0


def to_upper(str: str):

    """
        returns the uppercase version of the given string
        
        Args:
            str (str): the string that will be converted into uppercase

        Returns:
            new_str (str): the uppercase version of the input string
    """

    new_str = ''
    if ord(str[0:1]) >= 97 and ord(str[0:1]) <= 122:
        new_str = chr( ord(str[0:1]) - 32 ) + str[1:]
    else:
        new_str = str
    return new_str

def buy_ticket(filename: str, input: str) -> bool:

    """
        returns a boolean that tells the user if a given seat is taken or not, True if the seat is not taken, and False, if the seat is taken

        Args:
            filename (str): the file that has the data for taken and not taken seats
            input (str): the seat that the user wants to take, in the format of a letter and a number, where the letter is the row, and the number is the column.

        Returns:
            (bool): True, if the input seat is not taken, and False, if the input seat is taken
    """
    new_input = to_upper(input)
    column_num = int(new_input[1:]) - 1
    row_num = ord(new_input[0:1]) - 65
    data = create_list_letter(filename)
    if column_num - 1 < len(data[row_num]):

        if data[row_num][column_num] == "O":
            data[row_num][column_num] = 'X'
            output = open(filename, 'w')
            for row in data:
                output.write(' '.join(row) + '\n')
            output.close()
            return True
        else:
            return False
    return False
def main():
    assert sum_of_rows('numbers3.csv') == [15, 0, 0.2]

    assert sum_of_columns('numbers.csv') == [6, 12, 18]
    assert sum_of_columns('numbers2.csv') == [3.3, 4.4, 4.4]
    assert sum_of_columns('numbers3.csv') == [0.1, 5.1, 10, 0, 0, 0, 0]

    assert min_max_per_row('numbers.csv') == [(1, 3), (2, 6), (3, 9)]
    assert min_max_per_row('numbers2.csv') == [(1.1, 2.2),(1.1, 4.4), (1.1, 1.1) ]
    assert min_max_per_row('numbers3.csv') == [(0, 10), (0, 0), (0.1, 0.1)]

    assert average_of_columns('numbers.csv') == [2, 4, 6]
    assert average_of_columns('numbers2.csv') == [1.1, 2.2, 4.4]
    assert average_of_columns('numbers3.csv') == [0.03, 1.7, 3.33]

    table = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    zero_below(table, 2)
    assert table  == [[0, 2, 3], [2, 4, 6], [3, 6, 9]]
    table = [[1.1, 2.2], [1.1, 2.2, 4.4], [1.1]]
    zero_below(table, 1)
    assert table == [[1.1, 2.2], [1.1, 2.2, 4.4], [1.1]]
    table = [[0, 5, 10], [0, 0, 0, 0, 0, 0, 0], [0.1, 0.1]]
    zero_below(table, 10)
    assert table == [[0, 0, 10], [0, 0, 0, 0, 0, 0, 0], [0, 0]]
    

    assert buy_ticket('seats.txt', 'A10') == False
    assert buy_ticket('seats.txt', 'b3') == True
    assert buy_ticket('seats.txt', 'd3') == False

if __name__ == "__main__":
    main()




