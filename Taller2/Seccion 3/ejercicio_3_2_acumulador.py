
suma = 0
cantidad = 0

print("Ingresa números para sumar. Escribe 0 para terminar.\n")

while True:
    try:
        numero = float(input("Número: "))
        if numero == 0:
            break
        suma += numero
        cantidad += 1
    except ValueError:
        print("Por favor ingresa un número válido.")

print(f"\nCantidad de números ingresados: {cantidad}")
print(f"Suma total: {suma}")
