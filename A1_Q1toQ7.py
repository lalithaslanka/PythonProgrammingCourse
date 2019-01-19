# Assignment 1

#Question 1.1: Display 3 different messages
def displayMessages():
    print("Welcome to Python")
    print("Welcome to Computer Science")
    print("Programming is Fun")
    return

displayMessages()
###############################################


#Question1.2: Display a message 5 times
def displayMessageNtimes(n=5): 
    i=0
    while(i<5):
        print("Welcome to Python")
        i += 1
    return

displayMessageNtimes(5)

##################################################

#Question1.3: Display a pattern
def displayPattern():
    print("FFFFFFF    U     U    NN     NN")
    print("FF         U     U    NNN    NN")
    print("FFFFFFF    U     U    NN N   NN")
    print("FF          U   U     NN  N  NN")
    print("FF           UUU      NN    NNN")
    return


displayPattern()

##################################################

#Question 1.4: Write a program to display a table

def displayTable(a=4):
    print('\t' + "a"+'\t'+" a^2"+'\t'+"  a^3")
    for i in range(1,a+1):
        print('\t' + repr(i) +'\t' + " " + repr(i**2) + '\t' + "  "+ repr(i**3))
    return

displayTable()

##################################################

#Question 1.5: Compute the expression

def computeExpression():
    s = ((9.5*4.5) - (2.5*3))/(45.5 - 3.5)
    print("the value of the expression is ",s)
    return    

computeExpression()

####################################################

#Question 1.6 Display the result of the summation of the series

def sumOfSeries(n=9):
    sum=0
    for i in range(1,n+1):
        sum = sum + i
        
    print("The sum of the series is ",sum)
    return

sumOfSeries()
        
#########################################################

#Question 1.7 Calculate approximate value of PI


def approxPI(n=50):
    #get odd numbers from 2 to 50 and add them to the series
    seriesSum = 1
    operatorCount = True
    for num in range(2,n+1):
        if(num % 2) == 0:
            continue
        else:
            if(operatorCount):
                seriesSum = seriesSum - (1/num)
                operatorCount = False
                continue
            else:
                seriesSum = seriesSum + (1/num)
                operatorCount = True
                continue
    calculatedPI = 4 * seriesSum
    print("Value of PI is ", calculatedPI)
    return()

approxPI(100)
print("Value of PI till odd number 11")
approxPI(11)
print("Value of PI till odd number 15")
approxPI(15)

            
                  



















