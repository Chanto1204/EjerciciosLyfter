my_list = [9, 4, 7, 1, 5]
minor = my_list[0]

for index in range(len(my_list)):

    if my_list[index] < minor:
        minor = my_list[index]

print(f"El menor valor es {minor}")

    