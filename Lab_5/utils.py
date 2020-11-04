__doc__ = """
1
a) Write a module named utils.py that contains one function called process_item. The function will have one parameter, 
x, and will return the least prime number greater than x. When run, the module will request an input from the user, 
convert it to a number and it will display the output of the process_item function.
"""


def is_prime(x: int) -> bool:
    """

    :param x: integer
    :return: True, if x is prime, False otherwise
    """
    if x < 2 or x != 2 and x % 2 == 0 or x != 3 and x % 3 == 0:
        return False
    for d in range(5, 1 + int(x ** 0.5), 6):
        if x % d == 0 or x % (d + 2) == 0:
            return False
    return True
    return x > 1 and all(x % d for d in range(2, x))


def process_items(x: int) -> int:
    """
    The function will have one parameter, x, and will return the least prime number greater than x.

    :param x: an integer
    :return: the least prime number greater than x
    """
    while not is_prime(x + 1):
        x += 1
    return x + 1


if __name__ == "__main__":
    try:
        x = int(input("Enter a number\n"))
        print(process_items(x))
    except TypeError as e:
        print("Input is not integer", e)
    except Exception as e:
        print("Other error", e)

