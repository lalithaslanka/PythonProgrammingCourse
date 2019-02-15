#Design a class named QuadraticEquation for a quadratic equation
import math

class QuadraticEquation:
    
    def __init__(self, a = float(), b=float(), c=float()):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):        
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def getDiscriminant(self):
        a = self.__a
        b = self.__b
        c = self.__c
        discriminant = b**2 - (4*a*c)
        return discriminant

    def getRoot1(self):
        a = self.__a
        b = self.__b
        c = self.__c
        discriminant = self.getDiscriminant()
        if(discriminant >= 0):
            root1 = ((-1*b) + math.sqrt(discriminant))/(a*2)
            return root1
        else:
            print("complex roots")
            return 0

    def getRoot2(self):
        a = self.__a
        b = self.__b
        c = self.__c
        discriminant = self.getDiscriminant()
        if(discriminant >= 0):
            root2 = ((-1*b) - math.sqrt(discriminant))/(a*2)
            return root2
        else:
            print("complex roots") 
            return 0
        


#Test program for testing the QuadraticEquation class

user_a = float(input("Enter value of a"))
user_b = float(input("Enter value of b"))
user_c = float(input("Enter value of c"))

q1 = QuadraticEquation(user_a,user_b,user_c)

print(q1.get_a(), q1.get_b(), q1.get_c(), q1.getDiscriminant())
print("Root1 =",q1.getRoot1(),'\n', "Root2 = ",q1.getRoot2())




