
numeros = []
print("Ingresa 10 números:\n")

for i in range(1, 11):
    while True:
        try:
            num = float(input(f"Número {i}: "))
            numeros.append(num)
            break
        except ValueError:
            print("Por favor ingresa un número válido.")

sin_duplicados = []
for num in numeros:
    esta = False
    for existente in sin_duplicados:
        if existente == num:
            esta = True
            break
    if not esta:
        sin_duplicados.append(num)

print(f"\nLista original:         {numeros}")
print(f"Lista sin duplicados:   {sin_duplicados}")
print(f"Duplicados eliminados:  {len(numeros) - len(sin_duplicados)}")
