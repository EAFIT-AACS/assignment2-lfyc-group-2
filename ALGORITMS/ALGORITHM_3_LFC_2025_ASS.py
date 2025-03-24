#We import again the libraries that will be use, in this case, this one is used for handing exeptions
import sys

#We create the class PDA again but with the difference that in this case the main objetive is not determiate if a string is accepted or not, it is to build the generation configuration threes
class PushdownAutomaton:
    def __init__(self):
        self.states = {"q0", "q_accept"}
        self.input_alphabet = {"a", "b"}
        self.stack_alphabet = {"A", "Z0"}
        self.initial_state = "q0"
        self.accept_state = "q_accept"
        self.stack = ["Z0"]
        self.current_state = self.initial_state
    
    #Same function of the 2nd algorythm
    def transition(self, symbol):
        if self.current_state == "q0":
            if symbol == "a":
                self.stack.append("A")
                return True
            elif symbol == "b":
                if len(self.stack) > 1 and self.stack[-1] == "A":
                    self.stack.pop()
                    return True
                else:
                    return False
        return False

    #Same function of the 2nd algorythm but with the procces of the configuration threes
    def process_string(self, string):
        self.stack = ["Z0"]
        self.current_state = "q0"
        config_tree = [["q0", string if string else "ε", "".join(self.stack)]] # We build the configuration tree  taking into account: actual state, remaining input and stack

        # If the string its ε, it is automatically accepted
        if string == "":
            self.current_state = self.accept_state
            config_tree.append(["q_accept", "ε", "".join(self.stack)])
            return True, config_tree # We end the configuration three when the string is the ε string.
        
        # If is not the ε, we procces each char of the string
        for i, char in enumerate(string):
            remaining_input = string[i+1:]  # Remaning input
            if not self.transition(char):
                return False, []  # we verify again that all the transitions are valid.
            config_tree.append(["q0", remaining_input if remaining_input else "ε", "".join(self.stack)]) # If there is no more input left, we put the ε string and end the configuration three

        # if after the second verification of the accepted string, everithing is ok, we show the configuration three
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state
            config_tree.append(["q_accept", "ε", "".join(self.stack)])
            return True, config_tree
        return False, []

#In the main, we open the file with the accepted strings and we generate the configuration threes making a doble verification of the accepted strings
def main():
    try:
        with open("AcceptedStrings.txt", "r", encoding="utf-8") as file: # the utf-8 is used to handle the special characters that may appear
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'AcceptedStrings.txt'. Asegúrate de ejecutarlo primero.")
        sys.exit(1)

    #We show the configuration three in the console and we save it in a file called config_trees.txt for more order (it can be opened if wanted)
    print("\n--- Generating Configuration Trees for Accepted Strings ---\n")

    #We open the file and write the configuration threes generated
    with open("config_trees.txt", "w", encoding="utf-8") as output_file:
        output_file.write("Configuration Trees:\n\n")
        output_file.write("State, Remaining Input, Stack\n")

        for line in lines:
            line = line.strip().strip("'") #We remove the spaces and the ' that may appear in the strings to write them down in the file
            accepted, config_tree = PushdownAutomaton().process_string(line) #We generate the configuration three corresponding to the actual string

            # iF the string is accepted, we show it in the console and write it in the file
            if accepted:
                output_file.write(f"\nString: {line if line else 'ε'}\n")
                print(f"\nString: {line if line else 'ε'}\n")
                for entry in config_tree:
                    output_file.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
                    print(f"{entry[0]}, {entry[1]}, {entry[2]}")
                output_file.write("\n")
                print("\n")
                print(f"Processed configuration tree for: {line if line else 'ε'}")

if __name__ == "__main__":
    main()
