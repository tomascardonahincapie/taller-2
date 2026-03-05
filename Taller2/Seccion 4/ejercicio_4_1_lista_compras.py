
lista_compras = []

while True:
    print("\n=== Lista de Compras ===")
    print("1) Agregar producto")
    print("2) Eliminar producto")
    print("3) Mostrar lista")
    print("4) Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        producto = input("Nombre del producto: ").strip()
        if producto:
            lista_compras.append(producto)
            print(f"✅ '{producto}' agregado a la lista.")
        else:
            print("El nombre no puede estar vacío.")

    elif opcion == "2":
        if not lista_compras:
            print("La lista está vacía.")
        else:
            print("\nProductos en la lista:")
            for i, p in enumerate(lista_compras, 1):
                print(f"  {i}. {p}")
            producto = input("Nombre del producto a eliminar: ").strip()
            if producto in lista_compras:
                lista_compras.remove(producto)
                print(f"✅ '{producto}' eliminado de la lista.")
            else:
                print(f"❌ '{producto}' no está en la lista.")

    elif opcion == "3":
        if not lista_compras:
            print("\nLa lista de compras está vacía.")
        else:
            print(f"\nLista de compras ({len(lista_compras)} productos):")
            for i, p in enumerate(lista_compras, 1):
                print(f"  {i}. {p}")

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
