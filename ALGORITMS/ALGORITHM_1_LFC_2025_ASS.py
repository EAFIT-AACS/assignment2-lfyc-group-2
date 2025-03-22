#we import the libraries that will be used
import random

#This is the definition of the main function of this algorytm in wich the functions that generates the strings will be called"
def main():
    print("Welcome to the generator of strings!! How many strings would you like to create?")
    
    num_strings = int(input())
    
    if num_strings < 0:
        print("Please enter a valid integer (positive).")
        return
    
    valid_strings = set() #list in wich every string is unique
    invalid_strings = set() #list in wich every string is unique
    
    while len(valid_strings) < num_strings:
        valid_strings.add(generate_valid_string(random.randint(1,10)))
    
    while len(invalid_strings) < num_strings:
        invalid_strings.add(generate_invalid_string(random.randint(1,10))) #if the function generates a string that is already in the set, that one will be ignored and the function will generate a new one
    
    # We print in console the valid string and the in valid strings generated
    print("\n --- Valid Strings: ---\n")
    for j in valid_strings:
        print(j)
        
    print("\n --- InValid Strings: ---\n")
    for j in invalid_strings:
        print(j)
        
    # We save the valid and invalid strings in a txt file for it to be used in the next algorytmhs
        
    with open("String.txt", "w") as out_file:
        out_file.write("--- Valid Strings: ---\n")
        out_file.writelines(s + "\n" for s in valid_strings)
        
        out_file.write("\n --- InValid Strings: ---\n")
        out_file.writelines(s + "\n" for s in invalid_strings)
    
#In this function we create the string that belongs to the grammar: S → aSb | ε.
def generate_valid_string(n):
    if n == 0:
        return ""
    return "a" + generate_valid_string(n - 1) + "b"

#In this function we create the string that does not belong to the grammar: S → aSb | ε.
def generate_invalid_string(n):
    if n == 0:
        return ""
    return "a" + "b" + generate_valid_string(n - 1) + "a" + "b"

if __name__ == "__main__":
    main()




