# Lab_5 = None
from functions import anonymous_function, my_function, ex_3_v_1, ex_3_v_2, ex_3_v_3, ex_3_v_4, ex_4, ex_5, ex_6, \
    process, sum_digits, print_arguments, multiply_by_two

# Ex_2 = None
result_1 = anonymous_function(2, 3, d=2, e=3, a=1)
result_2 = my_function(2, 3, d=2, e=3, a=1)
print(result_1, result_2)


# Ex_3 = None
v_1 = ex_3_v_1("Programming in Python is fun")
v_2 = ex_3_v_2("Programming in Python is fun")
v_3 = ex_3_v_3("Programming in Python is fun")
v_4 = ex_3_v_4("Programming in Python is fun")
print(v_1, v_2, v_3, v_4, sep='\n')


# Ex_4 = None
print(ex_4(
    {1: 2, 3: 4, 5: 6},
    {'a': 5, 'b': 7, 'c': 'e'},
    {2: 3},
    [1, 2, 3],
    {'abc': 4, 'def': 5},
    3764,
    dictionar={'ab': 4, 'ac': 'abcde', 'fg': 'abc'},
    test={1: 1, 'test': True}
))


# Ex_5 = None
print(ex_5(
    [1, "2", {"3": "a"}, {4, 5}, 5, 6, 3.0]
))


# Ex_6 = None
print(ex_6(
    [1, 3, 5, 2, 8, 7, 4, 10, 9, 2]
))


# Ex_7 = None
print(
    process(
        filters=[lambda item: item % 2 == 0, lambda item: item == 2 or 4 <= sum_digits(item) <= 20],
        limit=2,
        offset=2
    )
)


# Ex_8 = None
# augmented_multiply_by_two = print_arguments(multiply_by_two)
# print(augmented_multiply_by_two())


# Ex_9 = None
