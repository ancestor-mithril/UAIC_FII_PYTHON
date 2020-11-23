import os
import random
import re
from typing import Pattern

from utilities import error_print, color_print
from utilities.utils import handle_user_input


def guessed(word: str, guessed_letters: set) -> bool:
    """

    :param word: word to be guessed
    :param guessed_letters: already guessed letters
    :return: True, if all word is guessed, False otherwise
    """
    for i in word:
        if i not in guessed_letters:
            return False
    return True


def word_print(word: str, guessed_letters: set):
    """

    :param guessed_letters: already guessed letters
    :param word: word to be printed
    :return: nothing
    """
    print("".join([i if i in guessed_letters else "_" for i in word]))


def play_game(category: str, folder: str):
    """

    :param category: a category, should be a file containing choosable words
    :param folder: folder from where to load category
    :return:
    """
    assert os.path.isfile(os.path.join(folder, category)), "chosen file is not valid"
    with open(os.path.join(folder, category), "r") as fd:
        choosable_words = eval(fd.read())
    word = random.choice(choosable_words)
    max_guesses = 5 if (len(word) - 2) > 6 else (len(word) - 2)
    guessed_letters = {word[0], word[-1]}
    guesses = 0
    pattern = re.compile(r"\w", re.IGNORECASE)
    while guesses < max_guesses and not guessed(word, guessed_letters):
        word_print(word, guessed_letters)
        color_print(f"Alegeti o litera. Litere deja alese: '{', '.join(guessed_letters)}'. Numar de ghiciri"
                    f":{guesses}/{max_guesses}")
        guessed_letter = handle_user_input(pattern).lower()
        if guessed_letter not in guessed_letters:
            guessed_letters.update(guessed_letter)
            if guessed_letter not in word:
                guesses += 1
        else:
            error_print(f"Letter {guessed_letter} already guessed")
    if guessed(word, guessed_letters):
        color_print(f"Felicitari, ai castigat, cuvantul corect este <<{word}>>! Numarul de incercari este "
                    f"{guesses}/{max_guesses}",
                    color="green")
    else:
        color_print(f"Cuvantul corect era <<{word}>>. Numar de incercari: {guesses}", color="red")

