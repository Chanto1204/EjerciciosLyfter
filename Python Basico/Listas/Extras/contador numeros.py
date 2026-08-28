my_list = [4, 2, 7, 2, 8, 2, 2]

counter = 0
number = int(input("Ingrese el número a buscar: "))

for index in range(len(my_list)):
    if my_list[index] == number:
        counter += 1

print(f"El número {number} aparece {counter} veces")     

