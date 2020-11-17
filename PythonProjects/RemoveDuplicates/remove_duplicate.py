"""C1: Remove Duplicates

Primind un folder la intrare, identificați toate fișierele duplicate (același conținut) din acel folder
și afișați o listă utilizatorului, cerându-i să decidă pe care dintre duplicate să le șteargă. În
funcție de decizia utilizatorului, fișierele duplicate vor fi șterse sau nu.
"""


import sys
from RemoveDuplicates.utils import get_duplicate_files, process_duplicates
from utilities.custom_error import CustomError
from utilities.utils import error_print


def run():
    """
    checks if minimum argv s are set
    path to target directory = the first argv
    optional recursive_walk = second argv
    duplicates = list of duplicate groups to be processed

    :return: nothing
    """
    if len(sys.argv) < 2:
        print("Execute the program as following:\n<your-path-to-python> remove_duplicate.py <folder> [-recursive_walk]")
        exit()
    path_to_directory = sys.argv[1]
    try:
        recursive_walk = (sys.argv[2] == "-recursive_walk")
    except IndexError:
        recursive_walk = False
    except Exception as e:
        error_print("Other error: {error}".format(error=e))
        exit("Error 2")
    try:
        duplicates = get_duplicate_files(path_to_directory, recursive_walk=recursive_walk)
        process_duplicates(duplicates)
    except CustomError as e:
        error_print("Error: {error}".format(error=e))
        exit("Error")
    except Exception as e:
        error_print("Other error: {error}".format(error=e))
        exit("Error 2")


if __name__ == "__main__":
    run()
