#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:
    def __init__(self, symbol, company_name):

        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name 
    
    def stock_purchase_history(self):
        

        aapl = Stock("AAPL", "Apple Inc")
        cat = Stock("CAT", "Caterpillar")
        ek = Stock("EK", "Eastman Kodak")
        goog = Stock("GOOG", "Google")
        msft = Stock("MSFT", "Microsoft")

        stock_dict = {
        aapl.get_symbol : aapl.get_company_name,
        cat.get_symbol : cat.get_company_name,
        ek.get_symbol : ek.get_company_name,
        goog.get_symbol : goog.get_company_name,
        msft.get_symbol : msft.get_company_name,
        }
        for stock in stock_dict:
            print (stock)
