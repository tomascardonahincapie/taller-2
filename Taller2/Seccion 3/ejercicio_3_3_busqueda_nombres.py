
nombres = ["Ana", "Carlos", "María", "Juan", "Lucía", "Pedro", "Sofía", "Miguel"]

print("Lista de nombres disponibles:")
for i in range(len(nombres)):
    print(f"  {i + 1}. {nombres[i]}")

buscar = input("\nIngresa el nombre a buscar: ")

encontrado = False
posicion = -1

for i in range(len(nombres)):
    if nombres[i].lower() == buscar.lower():
        encontrado = True
        posicion = i + 1
        break

if encontrado:
    print(f"\n✅ '{buscar}' encontrado en la posición {posicion}.")
else:
    print(f"\n❌ '{buscar}' no se encuentra en la lista.")
