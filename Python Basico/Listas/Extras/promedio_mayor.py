my_list = [10, 20, 30, 40, 50]


counter = 0

for index in range(len(my_list)):
    counter = counter + my_list[index] 

average = counter / len(my_list)

new_list = []

for index in range(len(my_list)):
    if my_list[index] > average:
        new_list.append(my_list[index])


print(f"Promedio: {average}")
print(f"Nueva lista: {new_list}")
