'''
credit card number verification algorithm
'''


#function that checks if the card type and the number entered match correctly
def cardtype_check(cardnum,cardtype):
    cardnum_str = str(cardnum)
    if(len(cardnum_str) >= 13 and len(cardnum_str) <= 16):
        if(cardtype.lower()=="visa" and cardnum_str[0] == "4"):
            cardtypeIsValid = True
        elif((cardtype.lower()=="mastercard" or cardtype.lower()=="master card" or cardtype.lower()=="master") and cardnum_str[0] == "5"):
            cardtypeIsValid = True
        elif((cardtype.lower()=="amex" or cardtype.lower()=="american" or cardtype.lower()=="american express") and cardnum_str[0:2] == "37"):
            cardtypeIsValid = True
        elif(cardtype.lower() == "discover" and cardnum_str[0] == "6"):
            cardtypeIsValid = True
        else:
            print("The card type and the number doesnt tally. Wrond card type entered.")
            cardtypeIsValid = False
    else:
        print("The card number doesnt have the correct number of digits. Wrong card Number")
        cardtypeIsValid = False
    return(cardtypeIsValid)


def sumOfDoubleEvenPlace(cardnum):
    cardnum_temp = cardnum
    sum_of_double_even= 0
    while (cardnum_temp >= 10):
        second_digit = cardnum_temp%100
        second_digit = int(second_digit/10)
        double_even = second_digit*2
        if(double_even >= 10):
            double_even = int(double_even/10) + (double_even%10)
        sum_of_double_even += double_even
        cardnum_temp = int(cardnum_temp/100)
    return(sum_of_double_even)

def sumOfOddPlace(cardnum):
    cardnum_temp = cardnum
    sum_of_odd = 0
    while (cardnum_temp>1):
        odd_digit = cardnum_temp%10
        sum_of_odd += odd_digit
        cardnum_temp = int(cardnum_temp/100)
    return(sum_of_odd)
        

def isValid(cardnum,cardType):
    card_valid = True
    if cardtype_check(cardnum,cardType):
        if ((sumOfDoubleEvenPlace(cardnum) + sumOfOddPlace(cardnum))%10 == 0):
            card_valid = True
        else:
            card_valid = False
    else:
        card_valid = False
    
    return (card_valid)


#main Program

type_of_card = input("Enter the type of credit card Visa or Master or Amex or Discover")
credit_card_no = eval(input("Enter your credit card number"))

card_validity = isValid(credit_card_no,type_of_card)
if card_validity:
    print("The card number you entered is correct")
else:
    print("The card number you enteres is invalid")

    
                      












































  
