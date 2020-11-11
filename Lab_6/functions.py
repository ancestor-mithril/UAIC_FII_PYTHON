import re
from typing import List
import os


def extract_words(input_text: str) -> List[str]:
    """
    Write a function that extracts the words from a given text as a parameter. A word is defined as a sequence of
    alpha-numeric characters.

    :param input_text:
    :return: all words from input_text
    """
    return re.findall(r"[a-zA-Z0-9]+", input_text)


def ex_2(regex: str, input_text: str, x: int) -> List[str]:
    """
    Write a function that receives as a parameter a regex string, a text string and a whole number x, and returns
    those long-length x substrings that match the regular expression.

    :param regex:
    :param input_text:
    :param x:
    :return:
    """
    return [i for i in re.findall(regex, input_text) if len(i) == x]


def ex_3(input_text: str, regex_list: List[str]) -> List[str]:
    """
    Write a function that receives as a parameter a string of text characters and a list of regular expressions and
    returns a list of strings that match on at least one regular expression given as a parameter.

    :param input_text:
    :param regex_list:
    :return:
    """
    match_list = []
    for i in regex_list:
        x = re.findall(i, input_text)
        for j in x:
            if j not in match_list:
                match_list.append(j)
    return match_list


def ex_4(path: str, attributes: dict) -> List[str]:
    """
    Write a function that receives as a parameter the path to an xml document and an attrs dictionary and returns those
    elements that have as attributes all the keys in the dictionary and values the corresponding values.

    :param path:
    :param attributes:
    :return:
    """
    match_list = []
    with open(path, "r") as file:
        xml_data = file.read()
        search_string = r"(<(\w+)" + r"".join(
            [" {key}=\"{value}\"".format(key=key, value=value) for key, value in attributes.items()]
        ) + r">[^</\2>]*</\2>)"
        print(search_string)
        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    return match_list


def ex_5(path: str, attributes: dict) -> List[str]:
    """
    Write another variant of the function from the previous exercise that returns those elements that have at least one
    attribute that corresponds to a key-value pair in the dictionary.

    :param path:
    :param attributes:
    :return:
    """
    match_list = []
    with open(path, "r") as file:
        xml_data = file.read()
        search_string = r"(<(\w+) [^>]*(" + r"|".join(
            ["{key}=\"{value}\"".format(key=key, value=value) for key, value in attributes.items()]
        ) + r")[^>]*>[^(<\2>)]*</\2>)"
        print(search_string)
        match_list += [x[0] for x in re.findall(search_string, xml_data)]
    return match_list


def censor_text(input_text: str) -> str:
    """

    :param input_text:
    :return:
    """
    input_text = input_text.group(0)
    return "".join([input_text[i] if i % 2 == 0 else "*" for i in range(len(input_text))])


def ex_6(input_text: str) -> str:
    """
    Write a function that, for a text given as a parameter, censures words that begin and end with vowels. Censorship
    means replacing characters from odd positions with *.

    :param input_text:
    :return: censored_text
    """
    return re.sub(r"(a|e|i|o|u)\w+(a|e|i|o|u)", censor_text, input_text)


def get_days_from_month_regex(year: str, month: str) -> str:
    """

    :param year:
    :param month:
    :return: number of days from this month
    """
    days_per_month = [
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|1\d|2[0-8])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])",
        r"(0[1-9]|[1-2]\d|30)",
        r"(0[1-9]|[1-2]\d|3[0-1])"
    ]
    try:
        if int(year) % 4 == 0:
            days_per_month[1] = r"(0[1-9]|1\d|2[0-9])"
        return days_per_month[int(month) - 1]
    except Exception as e:
        raise SystemError(e)


def get_control_digit(digits: str) -> str:
    """

    :param digits:
    :return: control digit
    """
    checksum_number = "279146358279"
    checksum = 0
    for i, j in zip(checksum_number, digits):
        checksum += int(i) * int(j)
    checksum %= 11
    if checksum == 10:
        checksum = 1
    return str(checksum)


def ex_7(input_text: str) -> bool:
    """

    :param input_text:
    :return: True, if input_text is CNP, False otherwise
    """
    match_first_digit = r"[1-8]"
    match_year = r"\d{2}"
    match_month = r"(0[1-9]|1[0-2])"
    match_day = get_days_from_month_regex(input_text[1:3], input_text[3:5])
    match_county = r"(0[1-9]|[1-3]\d|4[0-6]|5[1-2])"
    random_digits = r"(00[1-9]|0[1-9]\d|\d\d\d)"
    control_digit = get_control_digit(input_text[:-1])
    regex_string = r"^" + match_first_digit + match_year + match_month + match_day + match_county + random_digits + \
                   control_digit + r"$"
    print(regex_string)
    return bool(re.match(regex_string, input_text))


def ex_8(path: str, regex: str) -> List[str]:
    """

    :param path: path to directory
    :param regex:
    :return: List of files which name is regex or contain regex
    """
    match_list = []
    try:
        for root, d, f in os.walk(path):
            for i in f:
                file_path = os.path.join(root, i)
                bool_1 = re.match(regex, file_path)
                bool_2 = re.match(regex, open(file_path, "r").read())
                if bool_1 and bool_2:
                    match_list.append(">>" + file_path)
                elif bool_1 or bool_2:
                    match_list.append(file_path)
    except Exception as e:
        SystemError(e)
    return match_list

