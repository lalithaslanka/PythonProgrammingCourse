from tkinter import *

class InvestmentCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment calulator")

        Label(window, text = "Investment Amount").grid(row=1,column=1,sticky= W)
        Label(window, text = "No. of Years").grid(row=2,column=1,sticky= W)
        Label(window, text = "Annual Interest Rate").grid(row=3,column=1,sticky= W)
        Label(window, text = "Future Value").grid(row=4,column=1,sticky= W)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable = self.investmentAmountVar, justify = RIGHT).grid(row = 1, column = 2)

        self.numberOfYearsVar = StringVar()
        Entry(window, textvariable = self.numberOfYearsVar, justify = RIGHT).grid(row = 2, column = 2)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 3, column = 2)

        self.futureValueVar = StringVar()
        Label(window, textvariable = self.futureValueVar).grid(row = 4, column = 2)

        Button(window, text = "Calculate", command = self.calculateMoney).grid(row = 5, column = 2, sticky = E)

        window.mainloop()

    def calculateMoney(self):
        monthlyInterestRate = float(self.annualInterestRateVar.get())/(12*100)
        futureMoney = float(self.investmentAmountVar.get()) * (1 + monthlyInterestRate) **(float(self.numberOfYearsVar.get())*12)
        self.futureValueVar.set(format(futureMoney,"10.2f"))

InvestmentCalculator()

        



        



        
