class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        pi = 3.14
        area = pi * (self.radius ** 2) 
        return area



circle = Circle(5)

print(circle.get_area())