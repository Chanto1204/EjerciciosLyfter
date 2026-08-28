print("----Numero Mayor----")

number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))
number3 = int(input("Ingrese un ultimo numero: "))


if number1 >= number2 and number1 >= number3:
    print(f"El numero mayor es: {number1}")
elif number2 >= number1 and number2 >= number3:
    print(f"El numero mayor es: {number2}")
else: 
    print(f"El numero mayor es: {number3}")