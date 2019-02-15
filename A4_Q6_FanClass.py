# The Fan class) Design a class named Fan to represent a fan.
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed = SLOW, radius = 5.0, color = "blue", on = False):
        self.__speed = speed
        self.__on = on
        self.__color = color
        self.__radius = radius

    def getFanSpeed(self):
        return self.__speed

    def setFanSpeed(self, speed):
        self.__speed = speed

    def getFanOn(self):
        return self.__on

    def setFanOn(self, on):
        self.__on = on

    def getFanColor(self):
        return self.__color

    def setFanColor(self, color):
        self.__color = color

    def getFanRadius(self):
        return self.__radius

    def setFanRadius(self, radius):
        self.__radius = radius

#TEst Program to test Fan Class

fan1 = Fan('FAST', 10, "yellow", True)
fan2 = Fan('MEDIUM', 5) 

print(" Fan1 properties" ,'\n', "Speed: ", fan1.getFanSpeed(), " FanOn: ", fan1.getFanOn(), " Fancolor: ",fan1.getFanColor(), " Fan Radius : " , fan1.getFanRadius())

print(" Fan2 properties" ,'\n', "Speed: ", fan2.getFanSpeed(), " FanOn: ", fan2.getFanOn(), " Fancolor: ",fan2.getFanColor(), " Fan Radius : " , fan2.getFanRadius())





      














