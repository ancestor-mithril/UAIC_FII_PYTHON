from typing import List


def first_fibonacci(n: int) -> List[int]:
    """
    :param n: a natural integer
    :return: all fibonacci numbers \\leq n

    1. Write a function to return a list of the first n numbers in the Fibonacci string.
    """
    a = 0
    b = 1
    c = 0
    fibonacci_list = []
    while True:
        if a > n:
            return fibonacci_list
        fibonacci_list.append(a)
        c = a
        a = b
        b = b + c


def is_prime(n: int) -> bool:
    """
    :param n:
    :return: True, if number is prime, False otherwise
    """
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int((n ** 0.5)) + 1, 6):
        if n % i == 0:
            return False
    return True


def get_prime_list(number_list: List[int]) -> List[int]:
    """
    :param number_list: a list of numbers
    :return: same list with only prime numbers

    2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
    """
    return [x for x in number_list if is_prime(x)]


def list_operations(list_1, list_2) -> (List, List, List, List):
    """
    :param list_1:
    :param list_2:
    :return: intersection, reunion, a - b, b - a

    3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
    with b, a - b, b - a)
    """
    set_1 = set(list_1)
    set_2 = set(list_2)
    return list(set_1 | set_2), list(set_1 & set_2), list(set_1.difference(set_2)), list(set_2.difference(set_1))


def sing_song(notes: List[str], moves: List[int], start_position: int) -> List[str]:
    """
    4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers)
    and a start position (integer). The function will return the song composed by going though the musical notes
    beginning with the start position and following the moves given as parameter.

    :param notes: list of musical notes (strings)
    :param moves: list of integers
    :param start_position: starting note of song
    :return: song obtained through start_position and iteration of moves
    """
    return [notes[(start_position + sum(moves[:i])) % len(notes)] for i, x in enumerate([0] + moves)]


def modify_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
    elements under the main diagonal with 0 (zero).

    :param matrix:
    :return: matrix zeroed under the first diagonal
    """
    return [[matrix[i][j] if i >= j else 0 for i in range(len(matrix))] for j in range(len(matrix[0]))]


def ex_6(*lists: List, x: int) -> List:
    """
    6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
    containing the items that appear exactly x times in the incoming lists.

    :param lists: variable number of lists
    :param x: integer
    :return: list of elements appearing exactly x times
    """
    united_lists = []
    for i in lists:
        united_lists += i
    return list(set([i for i in united_lists if united_lists.count(i) == x]))


def is_palindrome(x: int) -> bool:
    """

    :param x: int
    :return: True, if x is palindrome, False otherwise
    """
    return str(x) == str(x)[::-1]


def get_palindromes(number_list: List[int]) -> (int, int):
    """
    7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
     The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
    :param number_list: list of numbers
    :return: (no_of_palindrome, greatest palindrome)
    """
    palindrome_list = list(filter(lambda x: str(x) == str(x)[::-1], number_list))
    return len(palindrome_list), max(palindrome_list)


def ex_8(string_list: List[str], x: int = 1, flag: bool = True) -> List[List[str]]:
    """
    Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
    True. For each string, generate a list containing the characters that have the ASCII divisible by x if the flag
    is set to True, otherwise it should contain characters that have the non-xvid ASCII code.

    :param string_list: a list of strings
    :param x:
    :param flag:
    :return: a list of characters with ASCII divisible with x or not
    """

    for i, string in enumerate(string_list):
        string_list[i] = [y for y in string if ord(y) % x == flag]
    return string_list


def are_smaller(i, j, matrix):
    """

    :param i:
    :param j:
    :param matrix:
    :return: True if i and j are smaller than elements on col before j
    """
    for x in range(len(matrix)):
        if x > i:
            return True
        if matrix[x][j] > matrix[i][j]:
            return False
    return True


def ex_9(matrix: List[List[int]]) -> list:
    """
    Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and
    will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
    A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats
    are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
    closest row from the field.

    :param matrix:
    :return: list of spectators that can't see
    """
    answer_and_none = [[(i, j) if (not are_smaller(i, j, matrix)) else None for j in range(len(matrix[0]))]
                       for i in range(len(matrix))]
    answer = []
    for i in answer_and_none:
        for j in i:
            if j is not None:
                answer.append(j)
    return answer


def index_in_list(a_list, index):
    """

    :param a_list:
    :param index:
    :return: True if index is in list, False otherwise
    """
    return index < len(a_list)


def ex_10(*input_lists: list) -> list:
    """
    10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first
    tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists,
    etc.

    :param input_lists: variable number of lists
    :return: list of touples of index elements in lists
    """
    return [tuple(y[z] if index_in_list(y, z) else None for y in input_lists) for z in
            range(max([len(x) for x in input_lists]))]


def ex_11(input_list: List[tuple]) -> List[tuple]:
    """
    11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
    tuple.

    :param input_list: list of tuples of strings
    :return: ordered list after 2nd element of tuples
    """
    input_list.sort(key=lambda x: x[1][2])
    return input_list
    # return sorted(input_list, key=lambda x: x[1][2])


def group_by_rhyme(input_words: List[str]) -> List[List[str]]:
    """
    12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
    grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.

    :param input_words: list of word
    :return: words grouped by rhyme
    """
    return [t for t in
            [[input_words[x] for x in range(y, len(input_words)) if input_words[x][-2:] == input_words[y][-2:] and
              input_words[x][-2:] not in [input_words[w][-2:] for w in range(y)]] for y in range(len(input_words))]
            if len(t) > 0]
