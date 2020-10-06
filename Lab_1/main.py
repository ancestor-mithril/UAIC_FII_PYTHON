#!/usr/bin/python3

import math
import numpy as np
import re


def biggest_common_divisor(number_list):
    """
    while list exists, calculate the gcd from former gcd and first element of list
    :param number_list: list of int
    :return: list gcd
    """
    x = number_list[0]
    y = number_list[1]
    number_list = number_list[2:]
    greatest_common_divisor = math.gcd(x, y)
    while len(number_list) > 0:
        greatest_common_divisor = math.gcd(x, number_list[0])
        number_list = number_list[1:]
    else:
        return greatest_common_divisor


def exercise_1():
    """
    Find The greatest common divisor of multiple numbers read from the console.
    """
    numbers = []
    x = input('Input a number\n')
    x = int(x)
    numbers.append(x)
    y = x
    while y > 1:
        y = int(input('Input a new number\n'))
        if y <= 1:
            break
        numbers.append(y)
    print("Gcd from ", numbers, " = ", biggest_common_divisor(numbers))


def count_vowels(target_string):
    """
    :param target_string: input string
    :return: number of vowels in the string
    """
    vowel_count = 0
    for char in target_string:
        for vowel in "aeiouAEIOU":
            if char == vowel:
                vowel_count += 1
    return vowel_count


def exercise_2():
    """
    Write a script that calculates how many vowels are in a string.
    """
    string_1 = "Adeghhhhhh"
    print("String ", string_1, " has ", count_vowels(string_1), " vowels")


def exercise_3():
    """
    Write a script that receives two strings and prints the number of occurrences of the first string in the second.
    """
    s_1 = "dadada"
    s_2 = "da"
    print(s_1.count(s_2))


def exercise_4():
    """
    Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
    """
    upper_case_string = "UpperCaseString"
    snake_case_string = ""
    if upper_case_string[0].isupper():
        snake_case_string += upper_case_string[0].lower()
        upper_case_string = upper_case_string[1:]
    for char in upper_case_string:
        if char.isupper():
            snake_case_string += "_" + char.lower()
        else:
            snake_case_string += char
    else:
        print(snake_case_string)


def get_spiral_string(target_matrix):
    """
    :param target_matrix: a square matrix
    :return: spiral string on matrix

    until the matrix is not empty, the first line, last column, last line, first column
    is removed from matrix and the elements are added to the string
    """
    spiral_string = ""
    while len(target_matrix) > 0:
        for i in target_matrix[0]:
            spiral_string += str(i)
        else:
            target_matrix = target_matrix[1:]
        # print(spiral_string, "1")
        if len(target_matrix) == 0:
            break
        for i in target_matrix:
            spiral_string += str((i[-1:])[0])
        else:
            target_matrix = target_matrix[:, :-1]
        # print(spiral_string, "2")
        if len(target_matrix) == 0:
            break
        reversed_last_line = ((target_matrix[-1:])[0])[::-1]
        for i in reversed_last_line:
            spiral_string += str(i)
        else:
            target_matrix = target_matrix[:-1]
        # print(spiral_string, "3")
        if len(target_matrix) == 0:
            break
        for i in target_matrix[::-1]:
            spiral_string += str(i[0])
        else:
            target_matrix = target_matrix[:, 1:]
        # print(spiral_string, "4")
    return spiral_string


def exercise_5():
    """
    Given a square matrix of characters write a script that prints the string obtained by going through the matrix
    in spiral order
    """
    spiral_matrix = np.array(
        [
            ["f", "i", "r", "s"],
            ["n", "_", "l", "t"],
            ["o", "b", "a", "_"],
            ["h", "t", "y", "p"]
        ]
    )
    print(get_spiral_string(spiral_matrix))


def is_palindrome(x):
    """
    :param x: an integer
    :return: True if x is palidrome, False otherwise

    X is transformed to a string and reversed
    """
    x = str(x)
    if x == x[::-1]:
        return True
    return False


def exercise_6():
    """
    Write a function that validates if a number is a palindrome.
    """
    input_number = input("Enter a number\n")
    input_number = int(input_number)
    if is_palindrome(input_number):
        print(input_number, " is palindrome")
    else:
        print(input_number, " is not palindrome")


def exercise_7():
    """
    Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this
    function will return 123, or if the text is "abc123abc" the function will extract 123). The function will
    extract only the first number that is found.
    """
    input_text = input('Enter a text with numbers inside\n')
    i = 0
    str_len = len(input_text)
    while i < str_len:
        if input_text[i].isdigit():
            first_number = ""
            while i < str_len and input_text[i].isdigit():
                first_number += input_text[i]
                i += 1
            else:
                print(int(first_number))
            break
        i += 1
    else:
        print(input_text + "\nhas no numbers")


def exercise_8():
    """
    Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format
    is 00011000, meaning 2 bits with value "1"
    """
    input_number = input("Enter a number\n")
    input_number = int(input_number)
    set_bits = bin(input_number).count("1")
    print(input_number, " has ", set_bits, " bits with value 1")


def exercise_9():
    """
    Write a functions that determine the most common letter in a string. For example if the string is "an apple is
    not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered.
    Casing should not be considered "A" and "a" represent the same character.
    """
    input_text = input("Enter a text\n")
    most_common_letter = ""
    no_of_apparitions = 0
    for i in input_text:
        if input_text.count(i) > no_of_apparitions:
            no_of_apparitions = input_text.count(i)
            most_common_letter = i
    if len(most_common_letter) == 1:
        print("\"", most_common_letter[0], "\"", " was found ", no_of_apparitions, " times")
    else:
        print("Hello there")


def exercise_10():
    """
    Write a function that counts how many words exists in a text. A text is considered to be form out of words that
    are separated by only ONE space. For example: "I have Python exam" has 4 words.
    """
    input_text = input("Enter a text\n")
    word_count = re.findall(r'\w+', input_text)
    print("There are ", len(word_count), " words")


# exercise_1()
# exercise_2()
# exercise_3()
# exercise_4()
# exercise_5()
# exercise_6()
# exercise_7()
# exercise_8()
# exercise_9()
exercise_10()
