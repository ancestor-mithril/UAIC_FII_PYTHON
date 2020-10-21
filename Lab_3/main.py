import functions as f

# ex_1
print(f.ex_1([1, 2, 3, 4, 5, 6, 4, 4, 3], [4, 5, 6, 7, 8, 8, 9]))

# ex_2
print(f.ex_2("aabbdkgrkf"))

# ex_3
print(f.ex_3(
    {'a': {'b': 0}, 's': 4, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1},
    {'a': {'a': 3}, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
))

# ex_4
print(f.build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))

# ex_5
print(f.validate_dict(
    {("l", "", "1", " "), ("s", "d", "3", "d")},
    {'a': {'a': "3"}, 's': "d3d", '.': "1", 'k': "1", 'h': "1", 'l': " 1 ", 'p': "2", ' ': "2", 'A': "1", 'n': "1"}
))

# ex_6
print(f.ex_6([1, 1, 2, 3]))

# ex_7
print(f.ex_7({1, 2}, {2, 3}))

# ex_8
print(f.ex_8({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# ex_9
print(f.ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
