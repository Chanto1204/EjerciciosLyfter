my_list = [3, 6, 0,-2, 4]

all_positive = True

for index in range(len(my_list)):
    if my_list[index] <= 0:
        all_positive = False
        break
    
if all_positive:
    print("Todos los números son positivos")
else:
    print("Hay al menos un número negativo o cero")