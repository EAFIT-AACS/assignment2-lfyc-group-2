import sys

class PushdownAutomaton:
    def __init__(self):
        # Definimos los estados
        self.states = {"q0", "q_accept"}
        self.input_alphabet = {"a", "b"}
        self.stack_alphabet = {"A", "Z0"}
        self.initial_state = "q0"
        self.accept_state = "q_accept"
        
        # Inicializamos la pila con el símbolo base Z0
        self.stack = ["Z0"]
        self.current_state = self.initial_state

    def transition(self, symbol):
        """Procesa un símbolo de entrada según las reglas del PDA"""
        if self.current_state == "q0":
            if symbol == "a":
                self.stack.append("A")  # Apilar 'A' por cada 'a'
                return True
            elif symbol == "b":
                if len(self.stack) > 1 and self.stack[-1] == "A":
                    self.stack.pop()  # Desapilar 'A' si se encuentra un 'b' válido
                    return True
                else:
                    return False  # Si no hay 'A' en la pila, la cadena es inválida
        return False  # Rechaza cualquier otro caso

    def process_string(self, string):
        """Procesa una cadena y determina si es aceptada por el PDA"""
        self.stack = ["Z0"]  # Reiniciar pila antes de cada verificación
        self.current_state = "q0"

        for char in string:
            if not self.transition(char):
                return False  # Si una transición falla, la cadena es inválida

        # Acepta solo si la pila vuelve a su estado inicial después de consumir la entrada
        if len(self.stack) == 1 and self.stack[0] == "Z0":
            self.current_state = self.accept_state
            return True
        return False

def main():
    try:
        with open("String.txt", "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'String.txt'.")
        sys.exit(1)

    pda = PushdownAutomaton()
    processing_strings = False
    accepted_strings = []
    print("\n--- Processing Strings with PDA ---\n")

    for line in lines:
        line = line.strip()
        if line.startswith("--- Strings: ---"):
            processing_strings = True
            continue
        if processing_strings and line:
            is_valid = pda.process_string(line)
            result = "Accepted ✅ by the PDA" if is_valid else "Rejected ❌ by the PDA"
            print(f"String: {line} -> {result}")
            if is_valid:
                accepted_strings.append(line)
    
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
