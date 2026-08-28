print("---Tabla de Multiplicar---")

number = int(input("Ingrese un número de 1 al 10: "))

for counter in range(1, 13):
    multiplier = counter * number
    print(f"{number} x {counter} = {multiplier}")



