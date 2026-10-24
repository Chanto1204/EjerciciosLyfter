from datetime import date

class User:

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth


    @property
    def age(self):
        today = date.today()

        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month:
            age -= 1
        
        elif today.month == self.date_of_birth.month:
            if today.day < self.date_of_birth.day:
                age -= 1
            
        return age


def validate_age(function):

    def wrapper(user):

        if user.age < 18:
            raise ValueError("El usuario es menor de edad")

        return function(user)

    return wrapper

@validate_age
def access_content(user):
    print("Acceso permitido")

user = User(date(2005, 12, 15))

#user = User(date(2020, 12, 15))


print(user.age)
access_content(user)