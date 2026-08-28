print("----Validación----")


number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))
number3 = int(input("Ingrese un ultimo numero: "))

if (number1 == 30 or number2 == 30 or number3 == 30) or (number1 + number2 + number3 == 30) :
    print("Correcto")
else:
    print("Incorrecto")