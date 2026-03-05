
print("=== Convertidor de Unidades ===")
print("1) Celsius → Fahrenheit")
print("2) Kilómetros → Millas")
print("3) Kilogramos → Libras")

opcion = input("\nSelecciona una opción (1-3): ")

if opcion == "1":
    try:
        celsius = float(input("Ingresa la temperatura en Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"\n{celsius}°C = {fahrenheit:.2f}°F")
    except ValueError:
        print("Por favor ingresa un número válido.")

elif opcion == "2":
    try:
        km = float(input("Ingresa la distancia en kilómetros: "))
        millas = km * 0.621371
        print(f"\n{km} km = {millas:.2f} millas")
    except ValueError:
        print("Por favor ingresa un número válido.")

elif opcion == "3":
    try:
        kg = float(input("Ingresa el peso en kilogramos: "))
        libras = kg * 2.20462
        print(f"\n{kg} kg = {libras:.2f} libras")
    except ValueError:
        print("Por favor ingresa un número válido.")

else:
    print("Opción no válida. Selecciona 1, 2 o 3.")
