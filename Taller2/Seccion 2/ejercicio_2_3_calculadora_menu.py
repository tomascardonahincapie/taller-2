
continuar = True

while continuar:
    print("\n=== Calculadora ===")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "5":
        print("Saliendo de la calculadora. ¡Hasta luego!")
        continuar = False
    elif opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
        except ValueError:
            print("Error: ingresa números válidos.")
            continue

        if opcion == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
    else:
        print("Opción no válida. Selecciona entre 1 y 5.")
