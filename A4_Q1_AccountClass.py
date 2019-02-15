class Account:
    '''
    Represents a class that creates an account with a account id and balance
    and has a said interest rates
    '''
    def __init__ (self, acc_id=0, acc_balance=100.0, acc_interest=0.0):
        self.__id = acc_id
        self.__balance = acc_balance
        self.__annualInterestRate = acc_interest

    def getId(self):
        return self.__id

    def setId(self, acc_id):
        self.__id = acc_id

    def getBalance(self):
        return self.__balance

    def setBalance(self, acc_balance):
        self.__balance = acc_balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, acc_interest):
        self.__annualInterestRate = acc_interest

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate/12)

    def getMonthlyInterest(self):
        interest = self.__balance * self.__annualInterestRate/(12*100)
        return interest

    def withdraw(self, amount):
        if(amount>self.__balance):
            print("Insufficient funds. Cannot withdraw. Enter a less amount")
            return False
        else:
            self.__balance -= amount
            print(self.__id, "#Account new balance is: ", self.__balance)
            return True       
            
    def deposit(self, amount):
        self.__balance += amount
        print("Amount deposited in #",self.__id, " The current balance is : ", self.__balance)

    
#Test Program to test AccountClass

#Account class Test Program
'''
 create a new account with account id of 1122, a balance of $20,000,
and an annual interest rate of 4.5%. Use the withdraw method to withdraw
$2,500, use the deposit method to deposit $3,000, and print the id, balance,
monthly interest rate, and monthly interest.
'''
#from A4_Q1_AccountClass import Account

account1 = Account(1122,20000,4.5)
account2 = Account(2324,34000,5.6)
print("The new account details:", account1.getId(), " Account Balance: ", account1.getBalance(), '\n', " Account INterest Rate: " , account1.getAnnualInterestRate() , "Monthly Interest: ", account1.getMonthlyInterest())
print("The new account details:", account2.getId(), " Account Balance: ", account2.getBalance(), '\n'," Account INterest Rate: " , account2.getAnnualInterestRate(),"Monthly Interest: ", account1.getMonthlyInterest())

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

    
        
    
