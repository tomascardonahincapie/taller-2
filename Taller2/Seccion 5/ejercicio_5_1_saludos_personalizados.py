
def saludar(nombre, hora):
    """Retorna un saludo personalizado según la hora del día."""
    if 5 <= hora <= 12:
        saludo = "¡Buenos días"
    elif 13 <= hora <= 19:
        saludo = "¡Buenas tardes"
    else:
        saludo = "¡Buenas noches"
    return f"{saludo}, {nombre}!"

nombre = input("Ingresa tu nombre: ").strip()

while True:
    try:
        hora = int(input("Ingresa la hora actual (0-23): "))
        if 0 <= hora <= 23:
            break
        else:
            print("La hora debe estar entre 0 y 23.")
    except ValueError:
        print("Por favor ingresa un número entero válido.")

mensaje = saludar(nombre, hora)
print(f"\n{mensaje}")
