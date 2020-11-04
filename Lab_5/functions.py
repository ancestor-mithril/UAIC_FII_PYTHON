import re
from typing import List


anonymous_function = lambda *args, **kwargs: sum(kwargs.values())


def my_function(*args, **kwargs):
    return sum(kwargs.values())


def ex_3_v_1(input_string: str) -> list:
    """

    :param input_string:
    :return: list of vowels from string
    """
    return [x for x in input_string if x in "aeiou"]


def ex_3_v_2(input_string: str) -> list:
    """

    :param input_string:
    :return: list of vowels from string
    """
    return list(filter(lambda x: x in "aeiou", input_string))


def ex_3_v_3(input_string: str) -> list:
    """

    :param input_string:
    :return: list of vowels from string
    """
    filter_array = [True if x in "aeiou" else False for x in input_string]
    return [i for (i, j) in zip(input_string, filter_array) if j]


def ex_3_v_4(input_string: str) -> list:
    """

    :param input_string:
    :return: list of vowels from string
    """
    return re.findall('[aeiou]', input_string)


def ex_4(*args, **kwargs) -> list:
    """
    4) Write a function that receives a variable number of arguments and keyword arguments. The function returns a list
     containing only the arguments which are dictionaries, containing minimum 2 keys and at least one string key with
     minimum 3 characters.

    :param args:
    :param kwargs:
    :return:
    """
    # valid_dictionaries = []
    # for i in args:
    #     if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2:
    #         valid_dictionaries.append(i)
    # for i in kwargs.values():
    #     if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2:
    #         valid_dictionaries.append(i)
    # return valid_dictionaries
    return [
               i for i in args
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ] + [
               i for i in kwargs.values()
               if type(i) == dict and len(i) > 1 and max([0] + [len(x) for x in i.keys() if type(x) == str]) > 2
           ]


def ex_5(input_list: list) -> list:
    """
    5) Write a function with one parameter which represents a list. The function will return a new list containing all
    the numbers found in the given list.

    :param input_list:
    :return: list with al numbers from given list
    """
    return re.findall(r"[0-9]+\.?[0-9]*", str(input_list))


def ex_6(input_list: List[int]) -> List[tuple]:
    """
    6) Write a function that receives a list with integers as parameter that contains an equal number of even and odd
    numbers that are in no specific order. The function should return a list of pairs (tuples of 2 elements) of numbers
    (Xi, Yi) such that Xi is the i-th even number in the list and Yi is the i-th odd number

    :param input_list:
    :return:
    """
    odd_numbers = [x for x in input_list if x % 2 == 0]
    even_numbers = [x for x in input_list if x % 2 == 1]
    return list(zip(odd_numbers, even_numbers))


def generate_fibonacci(n: int) -> list:
    """

    :param n:
    :return: list of n fibonacci
    """
    return_list = [0, 1]
    if n < 0:
        raise ValueError("generating first n fibonacci numbers failed, n is negative")
    else:
        for i in range(2, n):
            return_list.append(return_list[i - 2] + return_list[i - 1])
    return return_list[0:n]


def sum_digits(x):
    return sum(map(int, str(x)))


def process(**kwargs):
    """
    7) Write a function called process that receives a variable number of keyword arguments
    The function generates the first 1000 numbers of the Fibonacci sequence and then processes them in the following
    way: If the function receives a parameter called filters, this will be a list of predicates (function receiving an
    argument and returning True/False) and will retain from the generated numbers only those for which the predicates
    are True.
    If the function receives a parameter called limit, it will return only that amount of numbers from the sequence.
    If the function receives a parameter called offset, it will skip that number of entries from the beginning of the
    result list.
    The function will return the processed numbers.

    :param kwargs:
    :return:
    """
    fibonacci_sequence = generate_fibonacci(1000)
    try:
        if "filters" in kwargs.keys():
            for f in kwargs["filters"]:
                fibonacci_sequence = list(filter(f, fibonacci_sequence))
        if "offset" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[kwargs["offset"]:]
        if "limit" in kwargs.keys():
            fibonacci_sequence = fibonacci_sequence[:kwargs["limit"]]
    except Exception as e:
        print("Error at processing:", e)
    return fibonacci_sequence


def multiply_by_two(x):
    return x * 2


def print_arguments(functions: callable) -> callable:
    """
    8)
    a) Write a function called print_arguments with one parameter named function. The function will return one new
    function which prints the arguments and the keyword arguments received and will return the output of the function
    receives as a parameter.

    :param functions:
    :return:
    """
    function_string = """
def new_function(*args, **kwargs):
    print("Arguments are:", *args)
    print("Key arguments are:", **kwargs)
    return """ + str(functions).split()[1] + "(*args, **kwargs)"
    print(function_string)
    exec(function_string)
    print(new_function("1"))
    return new_function
