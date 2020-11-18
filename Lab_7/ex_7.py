"""
7. Write a script to simulate loto 6/49 draw (numbers extraction). The output should be a list of six numbers between 1
and 49 representing the winning combination.
"""


import random


lotto = [x + 1 for x in range(49)]
print(random.choices(lotto, k=6))

