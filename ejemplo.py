# Este es un pequeño programa de saludo en Python

def saludar_usuario():
    """
    Solicita el nombre del usuario y luego imprime un saludo personalizado.
    """
    nombre = input("¡Hola! ¿Cuál es tu nombre? ")
    print(f"¡Mucho gusto, {nombre}! Bienvenido a tu Codespace de Python en GitHub.")

    print("\n hola soy el nuevo miembro pasaba a saludarte")

# Llamar a la función para que el programa se ejecute
if __name__ == "__main__":
    saludar_usuario()