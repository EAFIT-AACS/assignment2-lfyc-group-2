#we import the libraries that will be used, in this case just random
import random

#This is the definition of the main function of this algorytm in wich the functions that generates the strings will be called"
def main():
    print("Welcome to the generator of strings!! How many strings would you like to create (per type - accepted and rejected)?")
    
    num_strings = int(input()) #The user inputs the number of strings that wants to generate
    
    if num_strings <= 0: #We create a verification of the number (must be positive)
        print("Please enter a valid integer (positive).")
        return
    
    valid_strings = set() #list in wich every string is unique
    invalid_strings = set() #list in wich every string is unique
    
    #We generate the strings taking into account the number given before
    while len(valid_strings) < (num_strings):
        valid_strings.add(generate_valid_string(random.randint(0,10)))
    
    while len(invalid_strings) < num_strings:
        invalid_strings.add(generate_invalid_string(random.randint(0,10))) #if the function generates a string that is already in the set, that one will be ignored and the function will generate a new one
    
    # We print in console the valid string and the in valid strings generated
    print("\n --- Strings: ---\n")
    for j in valid_strings:
        print("'" + j + "'")

    for j in invalid_strings:
        print("'" + j + "'")
        
    # We save the valid and invalid strings in a txt file for it to be used in the next algorytmhs
        
    with open("String.txt", "w") as out_file:
        out_file.write("--- Strings: ---\n")
        out_file.writelines("'" + s + "'" + "\n" for s in valid_strings)
        out_file.writelines("'" + s + "'" + "\n" for s in invalid_strings)
    
#In this function we create the string that belongs to the grammar: S → aSb | ε in a recusive way.
def generate_valid_string(n):
    if n == 0:
        return ""
    return "a" + generate_valid_string(n - 1) + "b"

#In this function we create the string that does not belong to the grammar: S → aSb | ε.
def generate_invalid_string(n):
    chars = ["a", "b"]
    return "".join(random.choices(chars, k=n)) + "a" # We add an "a" at the end of the string to make it invalid mandatorily (because of the random)

if __name__ == "__main__":
    main()