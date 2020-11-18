import hashlib
import os
import re
import time
import zipfile

import typing


def is_prime_most_efficient(x: int) -> bool:
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


def is_prime_not_efficient(x: int) -> bool:
    """

    :param x: integer
    :return: True, if x is prime, False otherwise
    """
    return x > 1 and all(x % d for d in range(2, x))


def test_time():
    """
    2. Write two functions to check if a number is prime, and check which of them is more time-efficient.

    :return:
    """
    prime_number = 999331 * 999331
    start = time.time()
    is_prime_most_efficient(prime_number)
    end = time.time()
    t1 = end - start
    start_2 = time.time()
    is_prime_not_efficient(prime_number)
    end_2 = time.time()
    t2 = end_2 - start_2
    print("most efficient: ", t1)
    print("least efficient: ", t2)


def are_equal(file_1: str, file_2: str, chunk_size: int = 1024) -> bool:
    """
    3. Write a function that will receive as parameters  two strings representing file paths and will return True if
    the files are identical or False otherwise.

    reads chunks of blocks for both files and checks them to be equal by comparing hashes

    :param chunk_size: size of chunk to be read
    :param file_1: path to file
    :param file_2: path to file
    :return: True, if files are equal, False otherwise
    """
    assert os.path.isfile(file_1) and os.path.isfile(file_2), "paths are not file"
    try:
        hash_1 = hashlib.sha1()
        hash_2 = hashlib.sha1()
        with open(file_1, 'rb') as fd_1:
            with open(file_2, 'rb') as fd_2:
                while True:
                    data_1 = fd_1.read(chunk_size)
                    data_2 = fd_2.read(chunk_size)
                    hash_1.update(data_1)
                    hash_2.update(data_2)
                    if not data_1 or not data_2:
                        break
        return hash_1.hexdigest() == hash_2.hexdigest()
    except Exception:
        raise


def ex_5(a_path: str, ext: str):
    """
    5. Write a function that receives two parameters: a_path and ext. The script will add all files from the a_path
    folder that have the extension ext to a zip archive named the.zip.

    :param a_path: path to a folder
    :param ext: extension of files
    :return:
    """
    z = zipfile.ZipFile("the.zip", "w", zipfile.ZIP_DEFLATED)
    assert os.path.isdir(a_path), "path is not dir"
    for root, directories, files in os.walk(a_path):
        for file_name in files:
            if os.path.isfile(os.path.join(root, file_name)) and os.path.splitext(file_name)[1][1:] == ext:
                try:
                    z.write(file_name)
                except Exception as e:
                    print(e)
                    pass


def ex_8(a_path: str, to_hextract: str) -> typing.Optional[str]:
    """
    8. Write a function that receives two parameters: a_path and to_hextract. If a_path is a valid zip archive and
    to_hextract  is a file inside the archive the function will return the md5 digest for unzipped content of to_hextract
    and None otherwise.

    :param a_path: path to a valid zip archive
    :param to_hextract: file inside a_path
    :return: md5 digest for unzipped to_hextract, if all is good. None, otherwise
    """
    try:
        assert zipfile.is_zipfile(a_path), "path is not zipfile"
        assert os.path.isfile(to_hextract), "to_hextract is not a file"
        z = zipfile.ZipFile(a_path)
        md5_file = hashlib.md5()
        with z.open(to_hextract, 'r') as fd:
            while True:
                data = fd.read(1024)
                md5_file.update(data)
                if not data:
                    break
        return md5_file.digest().decode('latin-1')
    except Exception as e:
        print(e)
        return None


def check_integrity(z: zipfile.ZipFile, i: zipfile.ZipInfo, pattern: typing.Pattern) -> bool:
    """

    :param pattern:
    :param z:
    :param i:
    :return:
    """
    with z.open(i.filename, "r") as fd:
        file_content = fd.read().decode('latin-1')
        data = re.match(pattern, file_content)
        content = data.group(1)
        hash_type = data.group(2)
        hexdigest = data.group(3)
        if hash_type == "md5":
            file_hash = hashlib.md5()
        elif hash_type == "sha256":
            file_hash = hashlib.sha256()
        elif hash_type == "sha512":
            file_hash = hashlib.sha512()
        else:
            return False
        file_hash.update(content.encode('latin-1'))
        return file_hash.hexdigest() == hexdigest


def ex_9(a_path: str) -> typing.List[typing.Tuple[str, bool]]:
    """

    :param a_path: path to directory
    :return: a list of tuples of filename and True, if file was compromised, False otherwise
    """
    assert zipfile.is_zipfile(a_path), "path is not a zipfile"
    pattern = re.compile(r"<CONTENT>(.*?)</CONTENT><SIGNATURE><TYPE>(.*?)</TYPE><HEXDIGEST>(.*?)</HEXDIGEST>"
                         r"</SIGNATURE>", flags=re.MULTILINE | re.DOTALL)
    z = zipfile.ZipFile(a_path)
    return [(i.filename, check_integrity(z, i, pattern)) for i in z.infolist() if i.filename[-1] != "/"]

