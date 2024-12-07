#add import

from question_a import Stock 

def stock_purchase_history():
   
    aapl = Stock('AAPL', 'Apple Inc')
    cat = Stock('CAT', 'Caterpillar')
    ek = Stock('EK', 'Eastman Kodak')
    goog = Stock('GOOG', 'Google')
    msft = Stock('MSFT', 'Microsoft')

    stk_dict = { 
                        aapl.get_symbol() : aapl.get_company_name(),
                        cat.get_symbol() : cat.get_company_name(),
                        ek.get_symbol() : ek.get_company_name(),
                        goog.get_symbol() : goog.get_company_name(),
                        msft.get_symbol() : msft.get_company_name()}
    for symbol, name in stk_dict.items():
       print(f"{symbol:<10} {name:<20}")
    

def menu():
    print("""     MENU   
1-Display stock purchase history
2-Exit
          """)
    choice = input('INPUT SELECTION 1 OR 2: ')
    if choice == "1":
        stock_purchase_history()
        menu()
    elif choice == '2':
        print("Exiting the program.")
        
    else:
            print("INVALID. Please input selection 1 or 2.")
            menu()

def main():
     menu()
main()