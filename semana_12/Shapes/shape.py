from abc import ABC, abstractmethod
from hmac import new
from math import pi

class Shape(ABC):
    def calculate_perimeter(self):
        pass


    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def calculate_perimeter(self):
        return 2*self.radius*pi
    
    def calculate_area(self):
        return (self.radius**2)*pi
    

class Square(Shape):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length
    
    def calculate_perimeter(self):
        return self.side_length*4
    
    def calculate_area(self):
        return (self.side_length**2)
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    
    def calculate_perimeter(self):
        return (self.length + self.width)*2
    
    def calculate_area(self):
        return self.length * self.width

new_circle = Circle(5)
new_square = Square(5)
new_rectangle = Rectangle(5,4)

print(f"The perimeter of a circle with radius {new_circle.radius} is {new_circle.calculate_perimeter():.2f}")
print(f"And its area is {new_circle.calculate_area():.2f}")
print()
print(f"The perimeter of a square with a side legth {new_square.side_length} is {new_square.calculate_perimeter():.2f}")
print(f"And its area is {new_square.calculate_area():.2f}")
print()
print(f"The perimeter of a rectangle with legth {new_rectangle.length} and {new_rectangle.width} is {new_rectangle.calculate_perimeter():.2f}")
print(f"And its area is {new_rectangle.calculate_area():.2f}")
print()