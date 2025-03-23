# We import the libraries that will be used, in this case this library is used for handling exceptions
import sys

# We create the class PDA which contains the initialization of the states and the transitions taking into account the grammar
class PushdownAutomaton:
    def __init__(self):
        # We define the constructor that initializes the attributes of the class when an instance of it is created
        self.states = {"q0", "q_accept"}
        self.input_alphabet = {"a", "b"}
        self.stack_alphabet = {"A", "Z0"}
        self.initial_state = "q0"
        self.accept_state = "q_accept"
        
        # We directly initialize the stack and initial state
        self.stack = ["Z0"]
        self.current_state = self.initial_state

    # We define the transitions that process character by character the string and determine if a string is accepted or rejected
    def transition(self, symbol):
        if self.current_state == "q0":  # Confirmation that the string is still being evaluated
            if symbol == "a":
                self.stack.append("A")  # Push 'A' onto the stack for each 'a' in the string
                return True  # Ends the transition
            elif symbol == "b": 
                if len(self.stack) > 1 and self.stack[-1] == "A":  # We check if the stack has an 'A' in the last position
                    self.stack.pop()  # Pop 'A' for each 'b' in the string
                    return True
                else:
                    return False  # If there is no 'A' left in the stack or the stack is empty, the string is invalid
        return False  # Reject the string in any other case (e.g., characters not in the alphabet)

    # We define the method that processes the string and determines if the string is accepted by the PDA
    def process_string(self, string):
        # We reset the stack and the current state before each verification
        self.stack = ["Z0"]
        self.current_state = "q0"

        # Special case: If the string is empty (ε), it is automatically accepted
        if string == "":
            self.current_state = self.accept_state
            return True

        # We iterate over the string (character by character) and check if it is accepted or rejected
        for char in string:
            if not self.transition(char):  # If the transition is not valid, the string is rejected
                return False  

        # A string is accepted if the only symbol left in the stack is the initial stack symbol 'Z0'
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state  # If the string is accepted, the current state is 'q_accept'
            return True
        return False

def main():
    # We open the file that contains the strings to be evaluated
    try:
        with open("String.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'String.txt'.")
        sys.exit(1)  # Exit the program if the file is not found

    # We create an instance of the class PushdownAutomaton and define the variables that will be used
    pda = PushdownAutomaton()
    processing_strings = False
    accepted_strings = []
    print("\n--- Processing Strings with PDA ---\n")

    # We check if the strings are accepted or rejected by the PDA
    for line in lines:
        line = line.strip().strip("'")  # Remove spaces and surrounding single quotes

        # We check if the line indicates the start of the strings to be evaluated
        if line == "--- Strings: ---":
            processing_strings = True
            continue
        
        if processing_strings:  # Process only non-empty lines
            is_valid = pda.process_string(line)  # Process the string and check if it is accepted or rejected
            result = "Accepted ✅ by the PDA" if is_valid else "Rejected ❌ by the PDA"
            print(f"String: '{line}' -> {result}")

            if is_valid:
                accepted_strings.append(line)
    
    # We save the accepted strings in a file for the third algorithm to construct the trees of accepted strings
    if accepted_strings:
        try:
            with open("AcceptedStrings.txt", "w") as output_file:
                output_file.write("--- Accepted Strings: ---\n")
                for string in accepted_strings:
                    output_file.write("'" + string + "'" + "\n")
            print("\n✅ Accepted strings have been successfully saved in 'AcceptedStrings.txt'.\n")
        except IOError:
            print("\n❌ Error: Unable to write to 'AcceptedStrings.txt'.\n")
    else:
        print("\n⚠️ No accepted strings to save. 'AcceptedStrings.txt' was not created.\n")

if __name__ == "__main__":
    main()
