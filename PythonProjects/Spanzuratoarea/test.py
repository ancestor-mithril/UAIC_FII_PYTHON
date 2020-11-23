import os
import re
import unittest
from Spanzuratoarea.build_game import run as build_game_run
import threading
import sys
from io import StringIO
import concurrent.futures


from Spanzuratoarea.utils import handle_user_input


class RemoveDuplicatesTesting(unittest.TestCase):
    def test_build_game(self):
        game_folder = "game_folder"
        words = {
            "sport": ["fotbal", "baschetbal", "handbal", "volei", "sah"],
            "masini": ["masina", "tir", "camion", "duba"]
        }
        thread = threading.Thread(target=build_game_run, args=(words,))
        thread.start()
        thread.join()
        for key in words.keys():
            with open(os.path.join(game_folder, key), "r") as fd:
                self.assertEqual(fd.read(), str(words[key]))


if __name__ == "__main__":
    unittest.main()
