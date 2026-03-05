
while True:
    try:
        n = int(input("Ingresa el valor de N: "))
        if n < 1:
            print("N debe ser un número positivo.")
        else:
            break
    except ValueError:
        print("Por favor ingresa un número entero válido.")

print(f"\nNúmeros pares del 1 al {n}:")
pares = []
for i in range(1, n + 1):
    if i % 2 == 0:
        pares.append(str(i))

print(", ".join(pares) if pares else "No hay números pares en ese rango.")
