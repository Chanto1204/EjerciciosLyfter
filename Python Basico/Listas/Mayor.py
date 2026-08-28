
my_list = []

for index in range(10):
    numbers = int(input("Ingrese un numero: "))
    my_list.append(numbers)

print(my_list)
print(f"El número mayor es: {max(my_list)}")