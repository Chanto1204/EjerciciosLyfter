print("----Suma de numero----")

sum_number= 0
counter = 1
number = int(input("Ingrese un numero: "))

for counter in range(1, number + 1):
    sum_number = sum_number + counter

print(f"La suma es {sum_number}")
