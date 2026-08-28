print("=======Calculadora========")
print("Tu numero a probar es")

def add(current_number):
    print("Sumar")
    while True:
        try: 
            number = float(input("ingrese un numero: "))
            return current_number + number
        except ValueError:
            print("Ingrese un numero correcto")
            print("Vuelve a intentar")

def subtract(current_number):
    print("Restar")
    while True:
        try:
            number = float(input("ingrese un numero: "))
            return current_number - number
        except ValueError:
            print("Ingrese un numero correcto")
            print("Vuelve a intentar")

def multiply(current_number):
    print("Multiplicar")
    while True:
        try:
            number = float(input("ingrese un numero: "))
            return current_number * number
        except ValueError:
            print("Ingrese un numero correcto")
            print("Vuelve a intentar")
        
def divide(current_number):
    print("Dividir")
    while True: 
        try:        
            number = float(input("ingrese un numero: "))
            return current_number / number
        except ValueError:
            print("Ingrese un numero correcto")
            print("Vuelve a intentar")
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")
            print("Vuelve a intentar")
            
def reset():
    return 0



def main():

    while True:
        try:
            current_number = float(input("Ingrese un primer número: "))
            break
        except ValueError:
            print("Ingrese un número válido.")
    
    option = 0
    
    while option != 6:
    
        print(f"Tu numero actual es: {current_number}")
        print("---Elige una opción---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Borrar resultado")
        print("6. Salir")
    
        try:
            option = int(input("Ingrese una opción:"))
        except ValueError:
            print("Ingrese una opción correcta ")
            continue
        
        if option == 1:
            current_number = add(current_number)
            print(f"Nuevo resultado: {current_number}")
    
        elif option == 2:
            current_number = subtract(current_number)
            print(f"Nuevo resultado: {current_number}")
            
        elif option == 3:
            current_number = multiply(current_number)
            print(f"Nuevo resultado: {current_number}")
    
        elif option == 4:
            current_number = divide(current_number)
            print(f"Nuevo resultado: {current_number}")
    
    
        elif option == 5:
            current_number = reset()
            print(f"Nuevo resultado: {current_number}")
    
        elif option == 6:
            print("Programa Terminado")
    
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()