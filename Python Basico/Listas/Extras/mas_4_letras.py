my_list = []

for index in range(5):
    word = input("Ingrese una palabra: ")
    my_list.append(word)

new_list = []

for index in range(len(my_list)):

    if len(my_list[index]) > 4:
        new_list.append(my_list[index])    

print(new_list)    