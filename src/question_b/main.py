#add import

from question_b import create_multiplication_table, display_multiplication_table


def main():
  while True: 

    multiplication_table = create_multiplication_table()
    

    print("Multiplication Table")

    display_multiplication_table(multiplication_table)

    user_input = input("Would you like to continue or quit? Enter 1 to continue or 2 to quit:")

    if user_input == '1':
        print("Let's continue!")
    elif user_input == '2':
        print("Exiting the program...Bye!")
        break
    
main()
    