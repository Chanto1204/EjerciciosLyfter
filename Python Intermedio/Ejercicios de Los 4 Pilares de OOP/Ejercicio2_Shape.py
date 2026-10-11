from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radio):
        self.radio = radio


    def calculate_area(self):
        area =  math.pi * self.radio ** 2
        return area
        

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radio
        return perimeter


class Square(Shape):
    def __init__(self, lado):
        self.lado = lado


    def calculate_area(self):
        area = self.lado ** 2
        return area
        

    def calculate_perimeter(self):
        perimeter = 4 * self.lado
        return perimeter


class Rectangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


    def calculate_area(self):
        area = self.base * self.height
        return area
        

    def calculate_perimeter(self):
        perimeter = 2 * (self.base + self.height)
        return perimeter


circle = Circle(5)
print("Círculo:")
print(circle.calculate_area())
print(circle.calculate_perimeter())

square = Square(5)
print("Cuadrado:")
print(square.calculate_area())
print(square.calculate_perimeter())

rectangle = Rectangle(8, 4)
print("Rectángulo:")
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())


#Figura	     Área	        Perímetro
#Círculo	 π × radio²	    2 × π × radio
#Cuadrado	 lado²	        4 × lado
#Rectángulo	 base × altura   2 × (base + altura)