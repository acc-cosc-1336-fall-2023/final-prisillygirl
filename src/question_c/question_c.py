#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):

        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol
    def get_company_name(self):
        return self.__company_name 
    

def get_stock_list():
    stock_list =[  
        Stock("AAPL", "Apple Inc"),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
    ]
    return stock_list
    
def create_stock_file():
    stock_data = [
        ("AAPL", "Apple Inc"),
        ("CAT", "Caterpillar"),
        ("EK", "Eastman Kodak"),
        ("GOOG", "Google"),
        ("MSFT", "Microsoft")
    ]
    
    with open("stock_file.dat", "w") as file:
        for symbol, company_name in stock_data:
            file.write(f"{symbol} {company_name}\n")
    print("stock_file.dat created with stock data")

create_stock_file()

def display_stock_report(stock_list):
     print("\n       Stock Report")
     print("Company Name\t\tSymbol")
     for stock in stock_list:
        print(f"{stock.get_company_name():<20} {stock.get_symbol()}")