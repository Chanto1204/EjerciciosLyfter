
grades_counter = 1
number_of_approving_grades = 0
number_of_failing_grades = 0
sum_of_failing_grades = 0
sum_of_approving_grades = 0
sum_of_all_grades = 0

total_grades = int(input("Ingrese la cantidad de notas: "))

while grades_counter <= total_grades:
    actual_grade = int(input(f"Ingrese la nota numero {grades_counter}: "))

    if actual_grade < 70:
        number_of_failing_grades = number_of_failing_grades + 1
        sum_of_failing_grades = sum_of_failing_grades + actual_grade
    else:
        number_of_approving_grades = number_of_approving_grades + 1
        sum_of_approving_grades = sum_of_approving_grades + actual_grade

    sum_of_all_grades = sum_of_all_grades + actual_grade
    grades_counter += 1


average_of_grades = sum_of_all_grades / total_grades

if number_of_approving_grades > 0:
    average_of_approving_grades = sum_of_approving_grades / number_of_approving_grades
else:
    average_of_approving_grades = 0
if number_of_failing_grades > 0:   
    average_of_failing_grades = sum_of_failing_grades / number_of_failing_grades
else:
    average_of_failing_grades = 0


print(f"El estudiante tiene {number_of_approving_grades} notas aprobadas")
print(f"Este es el promedio de notas aprobadas: {average_of_approving_grades} ")
print(f"El estudiante tiene {number_of_failing_grades} notas desaprobadas")
print(f"Este es el promedio de notas desaprobadas: {average_of_failing_grades}")
print(f"Este es el promedio total de notas: {average_of_grades}")
        


