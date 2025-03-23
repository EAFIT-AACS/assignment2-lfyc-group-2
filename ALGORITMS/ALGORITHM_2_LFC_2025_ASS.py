#We import the libraries that will be used, in this case this library is used for handing exeptions
import sys

#We create the class PDA wich contains the initizalization of the states and the transitions taking into account the grammar
class PushdownAutomaton:
    def __init__(self):

        # We define the constructor that "initializate" the atributtes of the class when ans intance of it its created
        self.states = {"q0", "q_accept"}
        self.input_alphabet = {"a", "b"}
        self.stack_alphabet = {"A", "Z0"}
        self.initial_state = "q0"
        self.accept_state = "q_accept" 
        
        # we directly initializate the stack and initial state
        self.stack = ["Z0"]
        self.current_state = self.initial_state

    # We define the transitions that process char by char the string and defines if a string accepted or rejected
    def transition(self, symbol):
        if self.current_state == "q0": #Confirmation that the string its not evaluated yet
            if symbol == "a":
                self.stack.append("A")  # stack 'A' for each 'a' in the string
                return True #Ends the transition
            elif symbol == "b": 
                if len(self.stack) > 1 and self.stack[-1] == "A": #We check if the stack has an 'A' in the last position for pre-confirmation
                    self.stack.pop()  # Unstack 'A' for each 'b' in the string
                    return True
                else:
                    return False  # If there is no 'A' left in the stack or the Stack is empty, the string is invalid
        return False  #Reject the string in any other case (strings with other characters that are not defined in the alphabet)

    #We define the method that process the string and determinate if the string is accepted by the PDA
    def process_string(self, string):
       
       #We reset the stack and the current state before each verification
        self.stack = ["Z0"] 
        self.current_state = "q0"

        #We iterate over the string (char by char) and check if the string is accepted or rejected
        for char in string:
            if not self.transition(char): #if the transition is not valid, the string is rejected 
                return False  # if one transition is invalid, the string is rejected (chars not in the alphabet)

        # A string is accepted if the only symbol left in the stack is the initial symbol of the same
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state #If the string is accepted, the current state is the accept state
            return True
        return False

def main():
    #We open the file that contains the strings to be evaluated
    try:
        with open("String.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'String.txt'.")
        sys.exit(1) #Exit the program if the file is not found (here we use the library sys)

    #We create an instance of the class PushdownAutomaton and we define the variables that will be used
    pda = PushdownAutomaton()
    processing_strings = False
    accepted_strings = []
    print("\n--- Processing Strings with PDA ---\n")

    #We check if the strings are accepted or rejected by the PDA
    for line in lines:
        line = line.strip()
        # We check if the line is the one that contains the strings to be evaluated (know when to start)
        if line.startswith("--- Strings: ---"):
            processing_strings = True
            continue
        if processing_strings and line:
            is_valid = pda.process_string(line) #We process the string and check if it is accepted or rejected
            result = "Accepted ✅ by the PDA" if is_valid else "Rejected ❌ by the PDA"
            print(f"String: {line} -> {result}")
            if is_valid:
                accepted_strings.append(line)
    
    #We save the accepted strings in a file for the third algorithm to contruct the "Threes" of the accepted strings
    if accepted_strings:
        try:
            with open("AcceptedStrings.txt", "w") as output_file:
                for string in accepted_strings:
                    output_file.write(string + "\n")
            print("\n✅ Accepted strings have been successfully saved in 'AcceptedStrings.txt'.\n")
        except IOError:
            print("\n❌ Error: Unable to write to 'AcceptedStrings.txt'.\n")
    else:
        print("\n⚠️ No accepted strings to save. 'AcceptedStrings.txt' was not created.\n")

if __name__ == "__main__":
    main()
