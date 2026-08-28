print("-----Descubriendo Edades-----")

name = input("Ingrese su nombre: ")
last_name = input("Ingrese su primer apellido: ")
age = int(input("Ingrese su edad: "))


if age <= 3: 
    print("Eres un bebé")
elif age <= 10:
    print("Eres un niño")
elif age <= 12:
    print("Eres un preadolescente")
elif age <= 17:
    print("Eres un adolescente")
elif age <= 29:
    print("Eres un adulto joven")
elif age <= 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor") 

