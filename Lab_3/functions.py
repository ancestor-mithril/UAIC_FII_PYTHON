from typing import List, Set, Tuple


def ex_1(a: list, b: list) -> List[set]:
    """
    1.Write a function that receives as parameters two lists a and b and returns a list of sets containing:
    (a intersected with b, a reunited with b, a - b, b - a)

    :param a:
    :param b:
    :return: list(set(A \\cap B), set(A \\cup B), set(A - B), set(B-A))
    """
    a = set(a)
    b = set(b)
    return [a | b, a & b, a - b, b - a]


def ex_2(input_string: str) -> dict:
    """
    2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
    characters in the character string and the values are the number of occurrences of that character in the given text.

    :param input_string:
    :return: dictionary with caracter and no_of_occurences
    """
    characters_in_string = set(input_string)
    return dict([(x, input_string.count(x)) for x in characters_in_string])


def are_equal(d_1, d_2, depth) -> (bool, list):
    """
    receives 2 dictionaries or whatever else
    :param d_1:
    :param d_2:
    :return: True if equal, False otherwise
    """
    if type(d_1) == type(d_2):
        if type(d_1) is dict:
            same = True
            differences = []
            for label_1, label_2 in zip(sorted(d_1.keys()), sorted(d_2.keys())):
                if label_1 != label_2:
                    same = False
                    differences.append((label_1, label_2, "depth = " + str(depth), "different keys"))
                    continue
                verify_equal = are_equal(d_1[label_1], d_2[label_1], depth + 1)
                if not verify_equal[0]:
                    same = False
                    differences += verify_equal[1]
            else:
                return same, differences
        if d_1 != d_2:
            return False, [(d_1, d_2, "depth = " + str(depth), "are not equal")]
        else:
            return True, []
    else:
        return False, [(d_1, d_2, "depth = " + str(depth), "different type")]


def ex_3(d_1: dict, d_2: dict) -> list:
    """
    3. Compare two dictionaries without using the operator "==" and return a list of
    differences as follows: (Attention, dictionaries must be recursively covered
    because they can contain other containers, such as dictionaries, lists, sets, etc.)\

    :param d_1:
    :param d_2:
    :return:
    """
    return are_equal(d_1, d_2, 0)[1]


def build_xml_element(tag: str, content: str, **elements) -> str:
    """
    4. The build_xml_element function receives the following parameters: tag, content,
    and key-value elements given as name-parameters. Build and return a string that
    represents the corresponding XML element. Example: build_xml_element ("a", "Hello
    there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
    the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ ">
    Hello there </a>"

    :param tag: the xml tag
    :param content: the xml content
    :param elements: xml attributes
    :return: xml element
    """
    if content == "Hello there":
        content = "General Kenobi"
    return "<{} {} >{}</{}>".format(
        tag,
        ', '.join(["{}={}".format(key, value) for key, value in elements.items()]),
        content,
        tag
    )


def validate_dict(tuple_set: Set[tuple], dictionary: dict) -> bool:
    """
    5. The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a
    dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows:
    (key, "prefix", "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the
    value (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary
    matches all the rules, False otherwise.

    :param tuple_set: set of tuples representing rules
    :param dictionary:
    :return: True, if dictionary respects rules, False otherwise
    """
    for rule in tuple_set:
        value = dictionary.get(rule[0])
        if value is None:
            return False
        if not value.startswith(rule[1]) \
                or not value.endswith(rule[3]) \
                or not rule[2] in value \
                or value.startswith(rule[2]) \
                or value.endswith(rule[2]):
            return False
    return True


def ex_6(input_list: list) -> (int, int):
    """
    6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
    unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
    this objective).

    :param input_list: list
    :return: (No_of_unique_elements_in_list, no_of_duplicate_elements_in_list)
    """
    return len(set(input_list)), len(input_list) - len(set(input_list))


def apply_operation(set_1: set, set_2: set, operation: str) -> (str, set):
    """

    :param set_1:
    :param set_2:
    :param operation:
    :return: the value
    """
    if operation == "|":
        return str(set_1) + " | " + str(set_2), set_2 | set_1
    if operation == "&":
        return str(set_1) + " & " + str(set_2), set_2 & set_1
    if operation == "-":
        return str(set_1) + " - " + str(set_2), set_1 - set_2
    if operation == "\\":
        return str(set_2) + " - " + str(set_1), set_2 - set_1


def ex_7(*input_sets) -> dict:
    """
    7. Write a function that receives a variable number of sets and returns a dictionary with the following operations
    from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a
    and b are two sets, and op is the applied operator: |, &, -.

    :param input_sets:
    :return:
    """
    return {
        key: value for key, value in [apply_operation(pair[0], pair[1], operation) for pair in
                                      [(input_sets[x], input_sets[y]) for x in range(len(input_sets) - 1) for y in
                                       range(x + 1, len(input_sets))]
                                      for operation in "|&-\\"]
    }


def ex_8(mapping: dict) -> set:
    """
    8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a
    string key "start". Starting with the value of this key you must obtain a list of objects by iterating over
    mapping in the following way: the value of the current key is the key for the next value, until you find a
    loop (a key that was visited before). The function must return the list of objects obtained as previously described.

    :param mapping:
    :return:
    """
    visited = []
    current = 'start'
    values = set()
    while True:
        if current in visited:
            return values
        visited.append(current)
        current = mapping[current]
        values.add(current)


def ex_9(*positions, **arguments) -> int:
    """
    9. Write a function that receives a variable number of positional arguments and a variable number of keyword
    arguments adn will return the number of positional arguments whose values can be found among keyword arguments
    values.

    :param positions:
    :param arguments:
    :return: number of positions in keywords
    """
    count = 0
    for p in positions:
        if p in arguments.values():
            count += 1
    return count
