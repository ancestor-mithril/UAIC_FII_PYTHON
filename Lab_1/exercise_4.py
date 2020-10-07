
import sys

upper_case_string = sys.argv[1]
snake_case_string = ""
if upper_case_string[0].isupper():
    snake_case_string += upper_case_string[0].lower()
    upper_case_string = upper_case_string[1:]
for char in upper_case_string:
    if char.isupper():
        snake_case_string += "_" + char.lower()
    else:
        snake_case_string += char
else:
    print(snake_case_string)