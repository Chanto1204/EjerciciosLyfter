import csv
from student import Student

def export_data(student_list):
    
    if not student_list:
        print("No hay estudiantes para exportar.")
        return

    with open("student.csv", 'w', encoding='utf-8', newline='') as csv_file:
    
        fieldnames = [
            "nombre",
            "sección", 
            "nota español", 
            "nota ingles", 
            "nota sociales", 
            "nota ciencias"
        ]

        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for student in student_list:
            student_data = {
                "nombre": student.name,
                "sección": student.section,
                "nota español": student.spanish_grade,
                "nota ingles": student.english_grade,
                "nota sociales": student.social_studies_grade,
                "nota ciencias": student.science_grade
        }
            writer.writerow(student_data)

def import_data(student_list):

    try:
        with open("student.csv", 'r', encoding='utf-8', newline='') as csv_file:
            student_list.clear()
            reader = csv.DictReader(csv_file)

            for student in reader:
                student["nota español"] = int(student["nota español"])
                student["nota ingles"] = int(student["nota ingles"])
                student["nota sociales"] = int(student["nota sociales"])
                student["nota ciencias"] = int(student["nota ciencias"])

                student_object = Student(
                    student["nombre"],
                    student["sección"],
                    student["nota español"],
                    student["nota ingles"],
                    student["nota sociales"],
                    student["nota ciencias"]
                )

                student_list.append(student_object)

    except FileNotFoundError:
        print("No se encontró el archivo.")