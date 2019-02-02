# Print a series of pentagonal numbers defined a n(3n-1)/2 when n is entered by the user

def getPentagonalNumber(n):
    pNumber = n * (3*n-1) /2
    return(pNumber)


def main():
    noOfnumbers = int(input(" Enter the number pentagonal numbers to display: "))
    while(noOfnumbers ==0):
        noOfnumbers = int(input(" You can't enter 0. Enter any integer: "))

    series = [int]
    for i in range(noOfnumbers):
        series.append(getPentagonalNumber(i+1))
    print(*series, sep = ", ")

main()    
        
        
