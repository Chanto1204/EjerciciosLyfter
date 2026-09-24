import actions
import data

def system_menu():

    student_list = []

    option = 0
    
    while option != 9:
    
        print("---Elige una opción---\n")
        print("---1. Añadir estudiante.")
        print("---2. Mostrar information de todos los estudiantes")
        print("---3. Mostrar el Top 3 de los mejores estudiantes")
        print("---4. Mostrar el promedio de notas total de los estudiantes")
        print("---5. Exportar datos CSV")
        print("---6. Importar datos CSV")
        print("---7. Eliminar un estudiante")#opcional
        print("---8. Mostrar lista de estudiantes reprobados")#opcional
        print("---9. Salir")
    
        try:
            option = int(input("Ingrese una opción:"))
        except ValueError:
            print("Ingrese una opción correcta ")
            continue
        
        if option == 1:
            print("----Ingrese los Datos del Estudiante----")
            actions.add_student(student_list)
    
        elif option == 2:
            print("----Información de Todos los Estudiantes----")
            actions.show_students(student_list)
            
        elif option == 3:
            print("----Top 3 de los Mejores Estudiantes----")
            actions.show_top_students(student_list)
            
        elif option == 4:
            print("----Promedio Total de Notas----")
            general_average = actions.calculate_general_average(student_list)
            if general_average is not None:
                print(f"El promedio general de los estudiantes es: {general_average}")

        elif option == 5:
            print("----Exportar datos a CSV----")
            data.export_data(student_list)
        elif option == 6:
            print("----Importar datos CSV----")
            data.import_data(student_list)
    
        elif option == 7:
            print("----Eliminar Estudiante Específico----")
            actions.delete_student(student_list)

        elif option == 8:
            print("----Lista de Estudiantes Reprobados----")
            actions.show_failed_students(student_list)
    
        elif option == 9:
            print("Programa Terminado")
            break
    
        else:
            print("Opción inválida.")