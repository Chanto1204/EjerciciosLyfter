"""def print_hello_world():
	print("Hello World!")
	print("Mi primera función")

print_hello_world()"""

def calculate_salary():
	worked_hours = int(input("Ingrese sus horas trabajadas: "))
	hour_rate = int(input("Ingrese su tarifa por hora: "))
	
	salary = worked_hours * hour_rate
	
	print(f'Su salario sera de {salary}')


calculate_salary()