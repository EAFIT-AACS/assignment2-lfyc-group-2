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
    
    while len(valid_strings) < num_strings:
        valid_strings.add(generate_valid_string(random.randint(1,10)))
    
    print("\nValid Strings:\n")
    for j in valid_strings:
        print(j)
    
"In this function we create the string that belongs to the grammar: S → aSb | ε."
def generate_valid_string(n):
    if n == 0:
        return ""
    return "a" + generate_valid_string(n - 1) + "b"

if __name__ == "__main__":
    main()
