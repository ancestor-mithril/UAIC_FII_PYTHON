import functions as f

1
print(f.first_fibonacci(100000))

# 2
print(f.get_prime_list(f.first_fibonacci(1000000)))

# 3
list_1 = [1, 2, 4, 6, 8]
list_2 = [2, 4, 5, 2, 6, 7]
print(f.list_operations(list_1, list_2))

# 4
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
print(f.sing_song(notes, moves, start_position))

5
matrix = [
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
print(f.modify_matrix(matrix))

# 6
print(f.ex_6([1, 2, 3], [1, 2, 3], [4, 4, 4], [5, 5, 5, 5], x=2))

# 7
print(f.get_palindromes([12321, 111, 231413, 14141]))

# 8
print(f.ex_8(["test", "hello", "lab002"], x=2, flag=False))

# 9
print(f.ex_9(
    [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 7, 2],
     [5, 5, 2, 5, 6, 4],
     [6, 6, 7, 6, 7, 5]]
)
)

# 10
print(f.ex_10([1, 2, 3], [5, 6, 7], ["a", "b", "c", 1]))


# 11
print(f.ex_11([('abc', 'bcd'), ('abc', 'zza')]))


# 12
print(f.group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
