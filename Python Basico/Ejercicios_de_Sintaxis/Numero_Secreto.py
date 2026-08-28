import random

print("-----Adivina el numero secreto-----")

secret_number = random.randint(1,10)

number = int(input("Ingrese un numero del 1 al 10: "))

while number != secret_number:
    print("El numero que ingresaste no es el correcto")
    number = int(input("Ingrese otro numero: "))

print("Felicidades adivinaste el numero secreto")


