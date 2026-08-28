print("---Comparador de tiempo---")

time = float(input("Ingrese un tiempo en segundos: "))

if time < 600:
    missing = 600 - time
    print(missing)
elif time == 600:
    print("Igual")
else:
    print("Mayor")