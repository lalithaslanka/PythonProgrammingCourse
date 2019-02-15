#Account class Test Program
'''
 create a new account with account id of 1122, a balance of $20,000,
and an annual interest rate of 4.5%. Use the withdraw method to withdraw
$2,500, use the deposit method to deposit $3,000, and print the id, balance,
monthly interest rate, and monthly interest.
'''

from A4_Q1_AccountClass import Account

account1 = Account(1122,20000,4.5)
account2 = Account(2324,34000,5.6)
print("The new account details:", account1.getId(), " Account Balance: ", account1.getBalance(), " Account INterest Rate: " , account1.getAnnualInterestRate())
print("The new account details:", account2.getId(), " Account Balance: ", account2.getBalance(), " Account INterest Rate: " , account2.getAnnualInterestRate())

#Test  for the withdrawMethod

if account1.withdraw(2500):
    print("Transaction Successful")
else:
    flag = True
    while flag:
        print ("Transaction unsuccessful. Do you want to try again?")
        response = input("If Yes press Y ")
        if response is 'Y' or 'y':
            withdrawl_amount = float(input("Enter the amount to withdraw"))
            transaction_status = account1.withdraw(withdrawl_amount)
            if transaction_status:
                print("Transaction Successful")
                flag = False
            else:
                continue
        else:
            print("Exiting the program")
            flag = False
            
#Test for deposit method

account1.deposit(3000)










    
    
