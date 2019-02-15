#Stock Class with Stock Symbol, Stock name,  previousClosingPrice, currentPrice,

class Stock:

    def __init__(self, stk_symbol = str(), stk_name= str(), previousPrice = float(), currentPrice= float()):
        self.__stk_symbol = stk_symbol
        self.__stk_name = stk_name
        self.__previousPrice = previousPrice
        self.__currentPrice = currentPrice

    def getStockSymbol(self):
        return self.__stk_symbol

    def getStockName(self):
        return self.__stk_name

    def getStockPreviousPrice(self):
        return self.__previousPrice

    def setStockPreviousPrice(self, price = float()):
        self.__previousPrice = price

    def getStockCurrentPrice(self):
        return self.__currentPrice

    def setStockCurrentPrice(self, price = float()):
        self.__currentPrice = price

    def getChangePercent(self):
        priceChange = self.__currentPrice - self.__previousPrice
        return priceChange/self.__previousPrice * 100
            
        
#Test program to test the Stock Class

intel = Stock("INTC", "Intel", 20.5, 20.35)
print ("Intel Stock details: ", intel.getStockSymbol(), " " , intel.getStockName(), " Prev.Closing " , intel.getStockPreviousPrice(), "Current  ", intel.getStockCurrentPrice())
print ("Percentage change in stock is ", intel.getChangePercent())

