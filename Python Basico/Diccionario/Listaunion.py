list_a = ["first_name","last_name", "role"]

list_b = ["Sebastian","Chanto","Software Engineer"]

my_dictionary = {}

for key, value in zip(list_a, list_b):
    my_dictionary[key] = value

print(my_dictionary)
