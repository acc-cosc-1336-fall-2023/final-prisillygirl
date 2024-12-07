#add import

from question_c import display_stock_report, get_stock_list


def main():
    
    while True:
       
        stock_list = get_stock_list()
    
        print("\n        Menu ")
        print("1. Display stock purchase history")
        print("2. Exit program")
        
        choice = input("Enter your choice 1 or 2: ")
        
        if choice == "1":
            display_stock_report(stock_list)
        elif choice == "2":
            print("Exiting the program...Bye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

main()