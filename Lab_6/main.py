from functions import extract_words, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7, ex_8


Ex_1 = None
print(extract_words("text, ana, are mere"))


Ex_2 = None
print(ex_2(r"\w+", "text, ana, are mere", 3))


Ex_3 = None
print(ex_3("text, ana, are mere", [r"\w\w\w", r"mere"]))


Ex_4 = None
print(ex_4("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))


Ex_5 = None
print(ex_5("example.xml", {"class": "url", "name": "url-form", "data-id": "item"}))


Ex_6 = None
print(ex_6("absefgei ara ara cha"))


Ex_7 = None
print(ex_7("1730110155203"))


Ex_8 = None
print(ex_8(".", ".*example.*"))
