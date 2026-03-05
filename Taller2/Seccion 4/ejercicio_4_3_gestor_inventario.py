
inventario = [
    {"nombre": "Manzana", "precio": 1500, "stock": 50},
    {"nombre": "Leche",   "precio": 3200, "stock": 30},
    {"nombre": "Pan",     "precio": 2800, "stock": 20},
]

def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print(f"\n{'Producto':<15} {'Precio':>10} {'Stock':>8}")
        print("-" * 35)
        for item in inventario:
            print(f"{item['nombre']:<15} ${item['precio']:>9,.0f} {item['stock']:>8}")

while True:
    print("\n=== Gestor de Inventario ===")
    print("1) Mostrar inventario")
    print("2) Agregar producto")
    print("3) Actualizar precio")
    print("4) Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        mostrar_inventario()

    elif opcion == "2":
        nombre = input("Nombre del producto: ").strip()
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
            inventario.append({"nombre": nombre, "precio": precio, "stock": stock})
            print(f"✅ Producto '{nombre}' agregado.")
        except ValueError:
            print("Error: precio y stock deben ser números.")

    elif opcion == "3":
        nombre = input("Nombre del producto a actualizar: ").strip()
        encontrado = False
        for item in inventario:
            if item["nombre"].lower() == nombre.lower():
                try:
                    nuevo_precio = float(input(f"Nuevo precio para '{item['nombre']}': "))
                    item["precio"] = nuevo_precio
                    print(f"✅ Precio actualizado a ${nuevo_precio:,.0f}.")
                    encontrado = True
                except ValueError:
                    print("Error: ingresa un precio válido.")
                break
        if not encontrado:
            print(f"❌ Producto '{nombre}' no encontrado.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
