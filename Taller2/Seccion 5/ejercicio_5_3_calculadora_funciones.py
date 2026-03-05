
def sumar(a, b):
    """Retorna la suma de a y b."""
    return a + b

def restar(a, b):
    """Retorna la resta de a y b."""
    return a - b

def multiplicar(a, b):
    """Retorna el producto de a y b."""
    return a * b

def dividir(a, b):
    """Retorna la división de a entre b. Valida división por cero."""
    if b == 0:
        return None
    return a / b

def pedir_numeros():
    """Solicita dos números al usuario y los retorna."""
    while True:
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            return a, b
        except ValueError:
            print("Por favor ingresa números válidos.")

def menu_calculadora():
    """Menú interactivo de la calculadora."""
    while True:
        print("\n=== Calculadora con Funciones ===")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División")
        print("5) Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "5":
            print("¡Hasta luego!")
            break
        elif opcion in ["1", "2", "3", "4"]:
            a, b = pedir_numeros()
            if opcion == "1":
                print(f"Resultado: {sumar(a, b)}")
            elif opcion == "2":
                print(f"Resultado: {restar(a, b)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(a, b)}")
            elif opcion == "4":
                resultado = dividir(a, b)
                if resultado is None:
                    print("Error: no se puede dividir entre cero.")
                else:
                    print(f"Resultado: {resultado}")
        else:
            print("Opción no válida.")

menu_calculadora()
