
from question_d import get_most_likely_ancestor_consensus


def main():
    while True:
       
        dna_string1 = input("Enter a DNA string between 9 and 16 characters: ")
        
        if len(dna_string1) < 9 or len(dna_string1) > 16:
            print("DNA string must be between 9 and 16 characters. Please enter between 9 and 16 characters.")
            continue
        
        
        dna_string2 = input("Enter a DNA substring of exactly 4 characters: ")
   
        if len(dna_string2) != 4:
            print("DNA substring must be exactly 4 characters. Please enter 4 characters.")
            continue
        
   
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        
    
        if result:
            print("Positions of the substring:", " ".join(map(str, result)))
        else:
            print(f"The substring '{dna_string2}' was not found in the DNA string.")
   
        user_choice = input("Do you want to continue? (y/n): ").strip().lower()
        if user_choice != 'yes':
            print("Exiting the program...Bye!")
            break
main()
