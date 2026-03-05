
def calcular_promedio(lista):
    """Calcula y retorna el promedio de una lista de números. Valida lista vacía."""
    if len(lista) == 0:
        return None
    suma = 0
    for num in lista:
        suma += num
    return suma / len(lista)

entrada = input("Ingresa los números separados por comas: ")

try:
    numeros = [float(n.strip()) for n in entrada.split(",") if n.strip()]

    promedio = calcular_promedio(numeros)

    if promedio is None:
        print("Error: no se ingresaron números.")
    else:
        print(f"\nNúmeros ingresados: {numeros}")
        print(f"Promedio: {promedio:.2f}")

except ValueError:
    print("Error: asegúrate de ingresar solo números separados por comas.")
