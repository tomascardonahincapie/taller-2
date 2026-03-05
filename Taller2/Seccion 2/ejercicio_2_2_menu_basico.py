
print("=== Menú Principal ===")
print("1) Saludar")
print("2) Despedirse")
print("3) Salir")

opcion = input("\nSelecciona una opción: ")

if opcion == "1":
    nombre = input("¿Cuál es tu nombre? ")
    print(f"\n¡Hola, {nombre}! ¿Cómo estás?")
elif opcion == "2":
    nombre = input("¿Cuál es tu nombre? ")
    print(f"\n¡Hasta luego, {nombre}! Que tengas un buen día.")
elif opcion == "3":
    print("\nSaliendo del programa. ¡Adiós!")
else:
    print("\nOpción no válida. Por favor selecciona 1, 2 o 3.")
