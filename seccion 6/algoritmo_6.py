
biblioteca = []

contador_id = 1

def agregar_libro():
    """Registra un nuevo libro validando año numérico y mayor a 1900."""
    global contador_id

    titulo = input("Título del libro: ").strip()
    autor  = input("Autor: ").strip()

    while True:
        try:
            anio = int(input("Año de publicación: "))
            if anio <= 1900:
                print("El año debe ser mayor a 1900.")
            else:
                break
        except ValueError:
            print("Por favor ingresa un año numérico válido.")

    libro = {
        "id":          contador_id,
        "titulo":      titulo,
        "autor":       autor,
        "anio":        anio,
        "disponible":  True
    }
    biblioteca.append(libro)
    contador_id += 1
    print(f"\n✅ Libro '{titulo}' agregado con ID {libro['id']}.")


def mostrar_libros():
    """Muestra todos los libros en formato legible."""
    if not biblioteca:
        print("\nNo hay libros registrados.")
        return

    print(f"\n{'─'*65}")
    for libro in biblioteca:
        estado = "Disponible" if libro["disponible"] else "Prestado"
        print(f"ID: {libro['id']} - '{libro['titulo']}' "
              f"({libro['autor']}, {libro['anio']}) [{estado}]")
    print(f"{'─'*65}")


def buscar_libro():
    """Busca libros por título o autor mostrando coincidencias parciales."""
    termino = input("Ingresa título o autor a buscar: ").strip().lower()
    resultados = []

    for libro in biblioteca:
        if termino in libro["titulo"].lower() or termino in libro["autor"].lower():
            resultados.append(libro)

    if resultados:
        print(f"\n{len(resultados)} resultado(s) encontrado(s):")
        for libro in resultados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"  ID: {libro['id']} - '{libro['titulo']}' "
                  f"({libro['autor']}, {libro['anio']}) [{estado}]")
    else:
        print(f"\n❌ No se encontraron libros con '{termino}'.")


def prestar_libro(id_libro):
    """Cambia disponibilidad a False si el libro existe y está disponible."""
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if libro["disponible"]:
                libro["disponible"] = False
                print(f"✅ Libro '{libro['titulo']}' prestado correctamente.")
            else:
                print(f"❌ El libro '{libro['titulo']}' ya está prestado.")
            return
    print(f"❌ No existe un libro con ID {id_libro}.")


def devolver_libro(id_libro):
    """Cambia el estado de disponibilidad a True."""
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                libro["disponible"] = True
                print(f"✅ Libro '{libro['titulo']}' devuelto correctamente.")
            else:
                print(f"⚠️  El libro '{libro['titulo']}' ya estaba disponible.")
            return
    print(f"❌ No existe un libro con ID {id_libro}.")


def eliminar_libro(id_libro):
    """Elimina un libro solo si no está prestado actualmente."""
    for libro in biblioteca:
        if libro["id"] == id_libro:
            if not libro["disponible"]:
                print(f"❌ No se puede eliminar '{libro['titulo']}' porque está prestado.")
            else:
                biblioteca.remove(libro)
                print(f"✅ Libro '{libro['titulo']}' eliminado del catálogo.")
            return
    print(f"❌ No existe un libro con ID {id_libro}.")

def libros_por_autor(autor):
    """Lista todos los libros de un autor específico."""
    autor_lower = autor.lower()
    resultados = [l for l in biblioteca if autor_lower in l["autor"].lower()]

    if resultados:
        print(f"\nLibros de '{autor}':")
        for libro in resultados:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"  ID: {libro['id']} - '{libro['titulo']}' ({libro['anio']}) [{estado}]")
    else:
        print(f"❌ No hay libros del autor '{autor}'.")


def estadisticas():
    """Muestra estadísticas del sistema: total, disponibles y prestados."""
    total      = len(biblioteca)
    disponibles = sum(1 for l in biblioteca if l["disponible"])
    prestados   = total - disponibles

    print("\n=== Estadísticas del Sistema ===")
    print(f"  Total de libros:      {total}")
    print(f"  Libros disponibles:   {disponibles}")
    print(f"  Libros prestados:     {prestados}")


def exportar_a_txt():
    """Guarda todos los libros en un archivo 'biblioteca.txt'."""
    try:
        with open("biblioteca.txt", "w", encoding="utf-8") as archivo:
            archivo.write("=== CATÁLOGO DE BIBLIOTECA ===\n\n")
            if not biblioteca:
                archivo.write("No hay libros registrados.\n")
            else:
                for libro in biblioteca:
                    estado = "Disponible" if libro["disponible"] else "Prestado"
                    linea = (f"ID: {libro['id']} - '{libro['titulo']}' "
                             f"({libro['autor']}, {libro['anio']}) [{estado}]\n")
                    archivo.write(linea)
            archivo.write(f"\nTotal de libros: {len(biblioteca)}\n")
        print("✅ Catálogo exportado a 'biblioteca.txt'.")
    except IOError as e:
        print(f"❌ Error al exportar: {e}")


def pedir_id(accion):
    """Solicita un ID numérico al usuario."""
    while True:
        try:
            return int(input(f"ID del libro a {accion}: "))
        except ValueError:
            print("Por favor ingresa un número entero válido.")


def menu_principal():
    """Menú interactivo con bucle while hasta que se seleccione salir."""
    while True:
        print("\n" + "═"*40)
        print("   SISTEMA DE GESTIÓN DE BIBLIOTECA")
        print("═"*40)
        print("1)  Agregar libro")
        print("2)  Mostrar todos los libros")
        print("3)  Buscar libro")
        print("4)  Prestar libro")
        print("5)  Devolver libro")
        print("6)  Eliminar libro")
        print("7)  Libros por autor")
        print("8)  Estadísticas")
        print("9)  Exportar a TXT")
        print("10) Salir")
        print("═"*40)

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            mostrar_libros()
            prestar_libro(pedir_id("prestar"))
        elif opcion == "5":
            mostrar_libros()
            devolver_libro(pedir_id("devolver"))
        elif opcion == "6":
            mostrar_libros()
            eliminar_libro(pedir_id("eliminar"))
        elif opcion == "7":
            autor = input("Ingresa el nombre del autor: ").strip()
            libros_por_autor(autor)
        elif opcion == "8":
            estadisticas()
        elif opcion == "9":
            exportar_a_txt()
        elif opcion == "10":
            print("\n¡Hasta luego! Cerrando el sistema de biblioteca.")
            break
        else:
            print("Opción no válida. Selecciona entre 1 y 10.")


if __name__ == "__main__":
    menu_principal()
