#The Rectangle class) Design a class named Rectangle to represent a rectangle.  

class Rectangle:

    def __init__(self, width = 1.0, height = 2.0):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return 2 *(self.width + self.height)


#Test Progrsm to test the class Rectangle


r1 = Rectangle(4,40)
r2 = Rectangle(3.5,35.7)

#Display  Rectangle 1 properties
print("Rectangle 1 width = ", r1.width, " height = ", r1.height, " perimeter = ", r1.getPerimeter(), " Area = ", r1.getArea())

#Display Rectangle 2 properties
print("Rectangle 2 width = ", r2.width, " height = ", r2.height, " perimeter = ", r2.getPerimeter(), " Area = ", r2.getArea())
