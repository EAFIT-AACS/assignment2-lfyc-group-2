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
    
    def transition(self, symbol):
        """Procesa una transición en función del símbolo de entrada."""
        if self.current_state == "q0":
            if symbol == "a":
                self.stack.append("A")
                return True
            elif symbol == "b":
                if len(self.stack) > 1 and self.stack[-1] == "A":
                    self.stack.pop()
                    return True
                else:
                    return False  # Rechaza si hay más "b" que "a"
        return False  # Rechaza cualquier otro caso no válido

    def process_string(self, string):
        """Procesa una cadena y devuelve si es aceptada junto con su configuración."""
        self.stack = ["Z0"]
        self.current_state = "q0"
        config_tree = [["q0", string if string else "ε", "".join(self.stack)]]

        # Si la cadena es vacía, aceptamos directamente
        if string == "":
            self.current_state = self.accept_state
            config_tree.append(["q_accept", "ε", "".join(self.stack)])
            return True, config_tree
        
        # Procesar cada carácter de la cadena
        for i, char in enumerate(string):
            remaining_input = string[i+1:]  # Parte restante de la cadena
            if not self.transition(char):
                return False, []  # Si alguna transición es inválida, se rechaza
            config_tree.append(["q0", remaining_input if remaining_input else "ε", "".join(self.stack)])

        # Aceptar si la pila vuelve a su estado inicial
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state
            config_tree.append(["q_accept", "ε", "".join(self.stack)])
            return True, config_tree
        return False, []


def main():
    """Lee las cadenas aceptadas, genera los árboles de configuración y los guarda."""
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
            accepted, config_tree = PushdownAutomaton().process_string(line)

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
