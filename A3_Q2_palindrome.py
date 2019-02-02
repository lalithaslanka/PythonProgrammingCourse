'''
(Palindrome integer) Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654 
def reverse(number):

# Return true if number is a palindrome 
def isPalindrome(number):

Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
'''
#Function to reverse a number

def reverse(number):
    reverseNo = 0
    while(number>1):
        reverseNo = int((reverseNo*10) + (number%10))
        number = int(number/10)
    return(reverseNo)

#Function for verifying if a number is palindrome
def isPalindrome(number):
    if(number == reverse(number)): 
        palindrome='True'
    else:
        palindrome = 'False'
    return(palindrome)
        

def main():
    number = int(input("Enter an integer: "))
    if (isPalindrome(number)==1):
        print("The number " + repr(number) + " is Palindrome")
    else:
        print("The number " + repr(number) + " is not a Palindrome")
        

main()
        
