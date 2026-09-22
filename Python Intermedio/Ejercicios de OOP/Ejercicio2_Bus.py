class Person:

    def __init__(self, name):
        self.name = name
        self.age = 0


class Bus:

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):  
        if len(self.passengers) >=self.max_passengers:
            print("El bus está lleno")
            return

        self.passengers.append(person)

    def remove_passenger(self):
        if self.passengers:
            self.passengers.pop()
        else:
            print("El bus esta vacío")


bus_passenger = Bus(4)
person_1 = Person("Sebastian")
person_2 = Person("Juan")
person_3 = Person("Pedro")

bus_passenger.add_passenger(person_1)
bus_passenger. add_passenger(person_2)
bus_passenger. add_passenger(person_3)

bus_passenger.remove_passenger()

for passenger in bus_passenger.passengers:
    print(passenger.name)

