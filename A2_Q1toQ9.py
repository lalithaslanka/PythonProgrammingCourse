# Assignment 2


        

#Q1 Write a program to convert from celcius to farenheit

def celciusToFarenheit():
    degreeInC = eval(input("Enter a degree in Celcius: "))
    degreeInF = 9/5 *degreeInC + 32
    print(repr(degreeInC) + " degrees in C is " + repr(degreeInF) + " in Farenheit")
    return

#celciusToFarenheit()
    
#Q2 Compute the volume of the cylinder taking the radius and height as inputs

PI = 3.147

def cylinderMetrics():
    radius = eval(input("Enter the radius of the cylinder "))
    height = eval(input("Enter the height of the cylinder "))
    #areaOfCylinder = 2* PI * radius **2 + 2* PI * radius * height
    areaOfCylinder = PI * radius * radius
    volumeOfCylinder = areaOfCylinder * height
    print(" The area is " + repr(areaOfCylinder) + " The volume is " + repr(volumeOfCylinder))
    return

#cylinderMetrics()

#Q3 Convert Feet to Metres

def feetToMeters():
    metricInFeet = eval(input("Enter the value in Feet "))
    metricInMeters = metricInFeet * 0.305
    print(repr(metricInFeet) + " in Feet is " +repr(metricInMeters)+" in meters")
    return

#feetToMeters()

#Q4 Convert Pounds to Kilograms

def convertPoundsToKgs():
    weightInPounds = eval(input(" Enter the weight in Pounds"))
    weightInKgs = 0.454 * weightInPounds
    print(repr(weightInPounds) + " in Pounds is " +repr(weightInKgs)+" in Kilograms")
    return

#convertPoundsToKgs()


#Q5 Calculate the gratuity and total when the user enters subtotal and gratuity rate

def calculateGratuity():
    subtotal, gratuity_rate = input("Enter the subtotal and gratuity rate separated by tab or space :").split()
    subtotal = float(subtotal)
    gratuity_rate = float(gratuity_rate)
    total = (1+gratuity_rate/100)*subtotal
    gratuity = total-subtotal
    print("The gratuity is "+ repr(gratuity) + " and the total is "+ repr(total))

#calculateGratuity()

#Q6 Sum of the digits in the integer

def sumOfDigits():
    valid = True
    while(valid):
        number = eval(input("Enter a number between 1 to 1000"))
        if(number >= 1 and number <= 1000):
            temp=int(number)
            sum = 0
            while(temp>=1):
                digit = temp%10
                sum = sum+digit
                temp = int(temp/10)
            valid=False
        else:
            print("Please enter a number in the range 1 to 1000")
        
    print("sum of the digits in the number is " + repr(sum))

#sumOfDigits()

#Q7 Find the number of years and days the minutes convert to

def convertMinutes():
    minutes = eval(input("Enter the minutes"))
    hours = minutes/60
    days = hours/24
    years = days/365
    years_temp = years
    while(years_temp>1):
        years_temp = years_temp/10
    days_final = years_temp*365
    print( repr(minutes) + " is " + repr(int(years)) + "  years and " + repr(int(days_final))+ " days")

#convertMinutes()

#Q8 Calculate energy needed to heat waterM, mass of water from temperature, T1 to T2

def calculateEnergy():
    mass = eval(input("Enter the amount of water in kilograms: "))
    t1, t2 = input("Enter the initial and final temperatures of water").split()
    t1= float(t1)
    t2 = float(t2)
    if(t1<t2):
        energy = mass * (t2-t1) * 4184
    else:
        energy = mass* (t1-t2) * 4184
    print("The energy needed is " + repr(energy) )
    
##calculateEnergy()

#Q9 Calculate the wind chill temperature based on  a formula when Current temp, wind speed are entered. this formula is valid only for -58 to 41F temperatures

def windChillIndex():
    userInput = True
    while (userInput):
        temp = eval(input("Enter the current temperature in Farenheit "))
        if (temp >= -58 and temp<= 41):
            break;
        else:
            print("Enter a valid temperatue between -58F and 41F")
    while (userInput):
        wind_speed = eval(input("Enter the wind speed in miles per hour"))
        if(wind_speed >= 2):
            break;
        else:
            print("Enter a windspeed above 2Miles/hr")
    wind_chill_index = 35.74 +(0.6215*temp) - (35.74 * wind_speed**0.16) + (0.4275 * temp * wind_speed**0.16)
    print(" the wind chill index is ", wind_chill_index)

#windChillIndex()

#Menu selection for displaying the assignment questions
    
print(" Welcome to Assignment2!")
proceed = True
while(proceed):
    user_choice = eval(input("Enter the question number you want to run from 1 to 9"))
    if (user_choice == 1):
        celciusToFarenheit()
    elif (user_choice == 2):
        cylinderMetrics()
    elif(user_choice == 3):
        feetToMeters()
    elif(user_choice == 4):
        convertPoundsToKgs()
    elif (user_choice == 5):
        calculateGratuity()
    elif(user_choice == 6):
        sumOfDigits()
    elif(user_choice == 7):
        convertMinutes()
    elif(user_choice == 8):
        calculateEnergy()
    elif(user_choice == 9):
        windChillIndex()
    else:
        print("Enter only choice from 1 to 9")
    flag = input("Enter Y to proceed to another question or hit N to exit")
    if(flag == "Y" or flag == "y"):
        proceed = True
    elif(flag == "N" or flag == "n"):
        proceed = False
    else:
        print("Enter a valid answer Y or N")























    






































    


        






























          
    
