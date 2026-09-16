def validate_grade(subject):

    while True:
        try:
            grade = int(input(f"Ingrese la nota {subject}: "))

            if grade < 0 or grade > 100:
                print("La nota debe ser entre 0 y 100")
                continue

            return grade
            
        except ValueError:
            print("Debe ingresar un número entero.")


def is_valid_name(name):

    if not name:
        return False

    for character in name:
        if character.isdigit():

            return False

    return True
        
    
def is_valid_section(section):
    if not section:
        return False
    
    if len(section) < 2 or len(section) > 3:
        return False

    if not section[:-1].isdigit():
        return False
    
    if not section[-1].isalpha():
        return False
    
    return True


def student_exists(student_list, name, section):

    for student in student_list:
        if student["nombre"] == name and student["sección"] == section:
            return True

    return False


def add_student(student_list):

    while True:
        try:
            amount = int(input("Ingrese la cantidad de estudiantes que desea agregar: "))

            if amount <= 0:
                print("Debe ingresar una cantidad mayor que 0.")
                continue
            break

        except ValueError:
            print("Debe ingresar un número entero.")

    for number in range(amount):
        print("====Ingrese Datos del Estudiante====\n")
        while True:
            while True:
                name = input("Ingrese el nombre: ")
                if is_valid_name(name):
                    break
                else:
                    print("Ingrese un nombre válido")
    
            while True:
                    
                section = input("Ingrese la sección: ")
                if is_valid_section(section):
                    break
                else:
                    print("Ingrese una sección válida")
            if student_exists(student_list, name, section):
                print("El estudiante ya existe")
            else:
                break

        spanish_grade = validate_grade("Español")
        english_grade = validate_grade("Ingles")
        social_studies_grade = validate_grade("Sociales")
        science_grade = validate_grade("Ciencias")
        student = {
            'nombre': name,
            'sección': section,
            'nota español': spanish_grade,
            'nota ingles': english_grade,
            'nota sociales': social_studies_grade,
            'nota ciencias': science_grade
        }
        student_list.append(student)


def show_students(student_list):

    if not student_list:
        print("No hay estudiante de momento")
        return
    for student in student_list:
        print ("--Datos de Estudiante--")
        for keys, values in student.items():
            
            print (f"{keys}: {values}")


def calculate_student_average(student):

    average_note = (
        student["nota español"] 
        + student["nota ingles"] 
        + student["nota sociales"] 
        + student["nota ciencias"])
    
    average = average_note / 4
    
    return average


def calculate_general_average(student_list):
    total = 0

    if not student_list:
        print("No hay estudiante de momento")
        return
    
    for student in student_list:
        average = calculate_student_average(student)
        total = total + average  


    general_average = total / len(student_list)

    return general_average


def get_average(student):
    return student["promedio"]


def show_top_students(student_list):
    student_average = []
    if not student_list:
        print("No hay estudiantes de momento")
        return
    for student in student_list:
        average = calculate_student_average(student)
        name = student["nombre"]

        student_data = {
            'nombre': name,
            'promedio': average
        }

        student_average.append(student_data)

    student_average.sort(key=get_average, reverse=True)

    for index in range(min(3, len(student_average))):
        student = student_average[index]
        print(f"Top {index + 1}: {student['nombre']} - {student['promedio']}")


def delete_student(student_list):

    if not student_list:
        print("No hay estudiante de momento")
        return

    name = input("ingrese el nombre: ")
    section = input("Ingresa la sección: ")

    for student in student_list:

        if student['nombre'] == name and student['sección'] == section:
            while True:
                answer = input("Quiere eliminar el estudiante? (si/no): ")

                if answer == "si":
                    student_list.remove(student)
                    print("Estudiante eliminado")
                    return

                elif answer == "no":
                    print("Estudiante no eliminado")
                    return

                else:
                    print("Ingrese una respuesta valida")

    print("El estudiante que ingreso no existe")


def show_failed_students(student_list):
    student_failing = []
    if not student_list:
        print("No hay estudiantes de momento")
        return
    for student in student_list:
        failing_subjects = []
        if student['nota español'] < 60:
            grade = student['nota español']

            subject_data = {
                'materia': 'Español',
                'nota': grade
            }

            failing_subjects.append(subject_data) 

        if student['nota ingles'] < 60:
            grade = student['nota ingles']
            
            subject_data = {
                'materia': 'Ingles',
                'nota': grade
            }

            failing_subjects.append(subject_data) 

        if student['nota sociales'] < 60: 
            grade = student['nota sociales']
            
            subject_data = {
                'materia': 'Sociales',
                'nota': grade
            }
            
            failing_subjects.append(subject_data) 

        if student['nota ciencias'] < 60:
            grade = student['nota ciencias']
            
            subject_data = {
                'materia': 'Ciencias',
                'nota': grade
            }
            
            failing_subjects.append(subject_data) 

        if failing_subjects:  
            name = student["nombre"]
            section = student['sección']

            failing_student = {
                'nombre': name,
                'sección': section,
                'materias_reprobadas': failing_subjects

            }

            student_failing.append(failing_student)
    if not student_failing:
        print("No hay estudiantes reprobados de momento")
        return
    for student in student_failing:
        print(f"Estudiante reprobado:\n{student['nombre']} - {student['sección']}")
        for subject in student['materias_reprobadas']:
            print(f"{subject['materia']}: {subject['nota']}")
