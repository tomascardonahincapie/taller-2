
entrada = input("Ingresa números separados por comas: ")

try:
    numeros = [float(n.strip()) for n in entrada.split(",") if n.strip() != ""]

    if not numeros:
        print("No se ingresaron números válidos.")
    else:
        maximo = numeros[0]
        minimo = numeros[0]
        suma = 0

        for num in numeros:
            if num > maximo:
                maximo = num
            if num < minimo:
                minimo = num
            suma += num

        promedio = suma / len(numeros)

        print(f"\n--- Estadísticas ---")
        print(f"Cantidad de números: {len(numeros)}")
        print(f"Suma:     {suma}")
        print(f"Máximo:   {maximo}")
        print(f"Mínimo:   {minimo}")
        print(f"Promedio: {promedio:.2f}")

except ValueError:
    print("Error: asegúrate de ingresar solo números separados por comas.")
