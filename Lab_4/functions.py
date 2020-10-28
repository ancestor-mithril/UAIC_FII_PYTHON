from typing import List, Callable
import os
import sys


def ex_1(path: str) -> List[str]:
    """
    1)	Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
    Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
    dat ca parametru.

    :param path: path to directory
    :return: list of ordered extensions from directory
    """
    return sorted({os.path.splitext(f)[-1][1:] for f in os.listdir(path) if
                   os.path.isfile(f) and os.path.splitext(f)[-1].startswith(".")})


def ex_2(directory_path: str, file_path: str):
    """
    Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
    Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
    fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.

    :param directory_path: path to directory to be checked
    :param file_path: path to file to be written
    :return: nothing
    """
    with open(file_path, "w") as fd:
        [fd.write(os.path.abspath(f)) for f in os.listdir(directory_path) if os.path.isfile(f) and f.startswith("a")]


def ex_4():
    """
    4)	Să se scrie o funcție ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca argument la
    linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.

    :return: list of all unique ordered extensions from command line directory
    """
    directory_path = sys.argv[1]
    return sorted({os.path.splitext(f)[-1][1:] for f in os.listdir(directory_path) if
                   os.path.isfile(f) and os.path.splitext(f)[-1].startswith(".")})


def ex_5(target: str, to_search: str) -> List[str]:
    """
    5)	Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search și returneaza
    o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută
    doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director.
    Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj
    corespunzator.

    :param target: path to directory or file
    :param to_search: string to be searched in file(s)
    :return: list of file paths in which to_search was found
    """
    if os.path.isfile(target):
        if to_search in open(target, "r").read():
            return [os.path.abspath(target)]
    elif os.path.isdir(target):
        to_return = []
        for root, directories, files in os.walk(target):
            # print(files)
            to_return += [os.path.abspath(os.path.join(root, file_name)) for file_name in files if
                          os.access(os.path.join(root, file_name), os.R_OK) and to_search in
                          open(os.path.join(root, file_name), "r").read()]
            return to_return
    else:
        raise ValueError(target + ": is not a valid path to file or directory")


def error_callback(exception: Exception):
    """
    prints exception

    :param exception:
    :return:
    """
    print(exception)


def ex_6(target: str, to_search: str, callback: Callable):
    """
    6)	Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența
    că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare
    apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru

    :param target: path to directory or file
    :param to_search: strin got be searched in file(s)
    :param callback: function to print errors
    :return: list of file_pats in wich to search was found
    """
    if os.path.isfile(target):
        try:
            if to_search in open(target, "r").read():
                return [os.path.abspath(target)]
        except Exception as e:
            callback(e)
    try:
        if not os.path.isdir(target):
            raise ValueError(target + ": is not a valid path to file or directory")
        to_return = []
        for root, directories, files in os.walk(target):
            for file_name in files:
                try:
                    if to_search in open(os.path.join(root, file_name), "r").read():
                        to_return.append(os.path.abspath(os.path.join(root, file_name)))
                except Exception as e:
                    callback(e)
        return to_return
    except Exception as e:
        callback(e)


def ex_7(file_path: str) -> dict:
    """
    7)	Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer
    si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea
    fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False
    daca se poate citi din/scrie in fisier.

    :param file_path: path to file
    :return: dictionary with absolute file path, file size, file extension, can be read or written
    """
    return {
        "full_path": os.path.abspath(file_path),
        "file_size": os.path.getsize(file_path),
        "file_extension": os.path.splitext(file_path)[-1][1:],
        "can_read": os.access(file_path, os.R_OK),
        "can_write": os.access(file_path, os.W_OK),
    }


def ex_8(dir_path: str) -> List[str]:
    """
    8)	Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un
    director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina
    directorului dir_path.

    :param dir_path: path to directory
    :return: list of paths to file in directory root
    """
    return [os.path.abspath(f) for f in os.listdir(dir_path) if os.path.isfile(f)]
