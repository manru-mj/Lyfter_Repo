import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
        #print(f"New Cricle with radius {radius}")

    def get_area(self):
        print(f"The circle's area is {round(math.pi*self.radius**2,2)} for a radius {self.radius}")

try:
    my_circle = Circle(float(input("Enter the radius measure: ")))
    my_circle.get_area()
except ValueError:
    print("Not a valid value.")
