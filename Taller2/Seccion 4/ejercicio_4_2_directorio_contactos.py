
contactos = {}

while True:
    print("\n=== Directorio de Contactos ===")
    print("1) Agregar contacto")
    print("2) Buscar contacto")
    print("3) Eliminar contacto")
    print("4) Mostrar todos")
    print("5) Salir")

    opcion = input("\nSelecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ").strip()
        telefono = input("Teléfono: ").strip()
        if nombre and telefono:
            contactos[nombre] = telefono
            print(f"✅ Contacto '{nombre}' agregado.")
        else:
            print("El nombre y teléfono no pueden estar vacíos.")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ").strip()
        if nombre in contactos:
            print(f"✅ {nombre}: {contactos[nombre]}")
        else:
            print(f"❌ No se encontró el contacto '{nombre}'.")

    elif opcion == "3":
        nombre = input("Nombre a eliminar: ").strip()
        if nombre in contactos:
            del contactos[nombre]
            print(f"✅ Contacto '{nombre}' eliminado.")
        else:
            print(f"❌ No se encontró el contacto '{nombre}'.")

    elif opcion == "4":
        if not contactos:
            print("\nEl directorio está vacío.")
        else:
            print(f"\nDirectorio ({len(contactos)} contactos):")
            for nombre, tel in contactos.items():
                print(f"  {nombre}: {tel}")

    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
