"""C4. Statistics

Scrieti un script care va primi ca parametru un path catre un fisier cu extensia .csv in care vor
fi salvate pe coloane urmatoarele date : varsta, sex, IQ, nationalitate si care va calcula pentru
o coloana la alegere media, mediana, deviatia standard, min, max, cvartile, covarianta si
coeficientul de corelatie dintre varsta si IQ si va afisa relatia dintre cele doua variabile folosind
un “plot”.
"""
import sys

from Statistics.utils import plot_data, get_csv_data
from utilities import CustomError, error_print


def run():
    if len(sys.argv) < 2:
        print("Execute the program as following:\npython.exe main.py csv_file")
        exit()
    try:
        labels, data = get_csv_data(sys.argv[1])
        plot_data(labels, data)
    except CustomError as e:
        error_print(f"Error: {e}")
        exit("Error")
    except Exception as e:
        error_print(f"Other error: {e}")
        exit("Error 2")


if __name__ == "__main__":
    run()
