
continuar = True

while continuar:
    try:
        numero = int(input("\nIngresa el número para la tabla de multiplicar: "))
    except ValueError:
        print("Por favor ingresa un número entero válido.")
        continue

    print(f"\n=== Tabla del {numero} ===")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    respuesta = input("\n¿Deseas ver otra tabla? (s/n): ").lower()
    if respuesta != "s":
        continuar = False
        print("¡Hasta luego!")
