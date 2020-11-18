"""
1. Write a program that will write the minutes passed from the start, every x seconds, where x is random chosen at each
iteraton (from the inteval [a, b] , where a, b are arguments). The program will run infinitely.
"""


import sys
import time
import random

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Run the project as following:")
        print("python.exe ex_1.py a b")
        print("where a and b are integers")
        exit()
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("a and b are not integers")
        exit()

t = time.time()
x = random.randint(a, b)

while True:
    time.sleep(x)
    t2 = time.time()
    print((t2 - t) / 60)


