"""
Configuration:
    script parameters:
    firs n_lt oba_ htyp
"""

import sys
import numpy as np
import functions_lab_1 as f1


def get_spiral_string(target_matrix: list):
    """
    :param target_matrix:  a matrix
    :return: spiral string on matrix

    until the matrix is not empty, the first line, last column, last line, first column
    is removed from matrix and the elements are added to the string
    """
    spiral_string = ""
    while len(target_matrix) > 0:
        spiral_string += target_matrix[0]
        target_matrix = target_matrix[1:]
        if len(target_matrix) == 0:
            break
        spiral_string += "".join(x[-1] for x in target_matrix)
        target_matrix = [x[:-1] for x in target_matrix]
        if len(target_matrix) == 0:
            break
        spiral_string += target_matrix[-1][::-1]
        target_matrix = target_matrix[:-1]
        if len(target_matrix) == 0:
            break
        spiral_string += "".join(x[0] for x in target_matrix)[::-1]
        target_matrix = [x[1:] for x in target_matrix]
        if len(target_matrix) == 0:
            break
    return spiral_string


spiral_matrix = np.array(sys.argv[1:])
print(get_spiral_string(spiral_matrix))
