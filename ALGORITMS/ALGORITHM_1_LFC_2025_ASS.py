import random

def generate_valid_string(n):
    """Genera una cadena válida basada en la gramática S → aSb | ε."""
    if n == 0:
        return ""
    return "a" + generate_valid_string(n - 1) + "b"
