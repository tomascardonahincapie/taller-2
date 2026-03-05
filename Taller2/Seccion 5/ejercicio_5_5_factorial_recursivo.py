
def factorial(n):
    """
    Calcula el factorial de n de forma recursiva.
    Retorna None si n es negativo.
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

while True:
    try:
        n = int(input("Ingresa un número entero para calcular su factorial: "))
        break
    except ValueError:
        print("Por favor ingresa un número entero válido.")

resultado = factorial(n)

if resultado is None:
    print(f"\n❌ Error: el factorial no está definido para números negativos.")
else:
    print(f"\n{n}! = {resultado}")
