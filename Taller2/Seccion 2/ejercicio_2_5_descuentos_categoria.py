
try:
    precio = float(input("Ingresa el precio del producto: $"))
    categoria = input("Ingresa la categoría (A, B o C): ").upper()

    if categoria == "A":
        porcentaje = 20
    elif categoria == "B":
        porcentaje = 15
    elif categoria == "C":
        porcentaje = 10
    else:
        porcentaje = 0
        print("Categoría no reconocida. No se aplica descuento.")

    descuento = precio * (porcentaje / 100)
    total = precio - descuento

    print(f"\n--- Resumen de compra ---")
    print(f"Precio original: ${precio:.2f}")
    print(f"Categoría: {categoria} - Descuento: {porcentaje}%")
    print(f"Ahorro:    ${descuento:.2f}")
    print(f"Total a pagar: ${total:.2f}")

except ValueError:
    print("Error: ingresa un precio numérico válido.")
