class Employee:

    def work(self):
        print("Estoy trabajando")



class Student:

    def study(self):
        print("Estoy estudiando")

class Intern(Employee, Student):
    pass


intern = Intern()

intern.work()
intern.study()