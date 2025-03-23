import sys

class PushdownAutomaton:
    def __init__(self):
        self.states = {"q0", "q_accept"}
        self.input_alphabet = {"a", "b"}
        self.stack_alphabet = {"A", "Z0"}
        self.initial_state = "q0"
        self.accept_state = "q_accept"
        self.stack = ["Z0"]
        self.current_state = self.initial_state
    
    def transition(self, symbol, remaining_input):
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
    
    def process_string(self, string):
        self.stack = ["Z0"]
        self.current_state = "q0"
        config_tree = [["q0", string, "".join(self.stack)]]
        
        for i, char in enumerate(string):
            remaining_input = string[i+1:]  # Parte restante de la cadena a procesar
            if not self.transition(char, remaining_input):
                return False, []
            config_tree.append(["q0", remaining_input, "".join(self.stack)])
        
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state
            config_tree.append(["q_accept", "ε", "".join(self.stack)])
            return True, config_tree
        return False, []
    

def main():
    try:
        with open("AcceptedStrings.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'AcceptedStrings.txt'. Asegúrate de ejecutarlo primero.")
        sys.exit(1)

    print("\n--- Generating Configuration Trees for Accepted Strings ---\n")
    
    with open("config_trees.txt", "w", encoding="utf-8") as output_file:
        output_file.write("Configuration Trees:\n\n")
        output_file.write("State, Remaining Input, Stack\n")
        
        for line in lines:
            line = line.strip().strip("'")
            if line:
                accepted, config_tree = PushdownAutomaton().process_string(line)
                if accepted:
                    output_file.write(f"\nString: {line}\n")
                    for entry in config_tree:
                        output_file.write(f"{entry[0]}, {entry[1]}, {entry[2]}\n")
                    output_file.write("\n")
                    print(f"Processed configuration tree for: {line}")

if __name__ == "__main__":
    main()
