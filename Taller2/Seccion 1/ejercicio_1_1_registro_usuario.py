
nombre = input("Ingresa tu nombre: ")

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        if edad <= 0:
            print("La edad debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Por favor ingresa un número válido para la edad.")

ciudad = input("Ingresa tu ciudad: ")

print(f"\nHola {nombre}, tienes {edad} años y vives en {ciudad}.")
