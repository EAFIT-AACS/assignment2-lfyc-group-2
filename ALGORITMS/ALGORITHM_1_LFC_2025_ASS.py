def strings_into(n_string):
    print(n_string)

def main():
    print("Welcome to the generator of strings!! How many strings would you like to create?")
    
    try:
        num_strings = int(input())
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    strings_into(num_strings)
    
    # Abrimos un archivo txt en modo escritura en el que se cargarán las cadenas creadas
    # with open("String.txt", "w") as out_file:
    #     pass  # Aquí se puede escribir en el archivo si es necesario

if __name__ == "__main__":
    main()
