import errno
import string
import unittest
import os
import random
from RemoveDuplicates.utils import get_duplicate_files, are_equal


class RemoveDuplicatesTesting(unittest.TestCase):
    def test_get_duplicate_files(self):
        try:
            os.makedirs('test_folder/unit_test_dir')
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
        for i, j in enumerate("aaeiia"):
            with open(j + str(i), "w") as f:
                f.write(j)
        correct_result = [['a0', 'a1', 'a5'], ['i3', 'i4']]
        self.assertEqual(get_duplicate_files(".", recursive_walk=False), correct_result, "test duplicates in dir root")
        for i, j in enumerate("aaeiia"):
            os.remove(j + str(i))

    def test_are_equal(self):
        file_1 = "file_1"
        file_2 = "file_2"
        random_string = ''.join(random.choices(string.ascii_uppercase, k=100))
        with open(file_1, "w") as f:
            f.write(random_string)
        with open(file_2, "w") as f:
            f.write(random_string)
        self.assertTrue(are_equal(file_1, file_2), "same random text")
        with open(file_2, "a+") as f:
            f.write("a")
        self.assertFalse(are_equal(file_1, file_2), "nearly same random text")
        os.remove(file_1)
        os.remove(file_2)


if __name__ == "__main__":
    unittest.main()
