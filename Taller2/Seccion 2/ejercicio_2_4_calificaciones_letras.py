
while True:
    try:
        nota = float(input("Ingresa la nota (0 - 100): "))
        if nota < 0 or nota > 100:
            print("La nota debe estar entre 0 y 100.")
        else:
            break
    except ValueError:
        print("Por favor ingresa un número válido.")

if nota >= 90:
    letra = "A"
    descripcion = "Excelente"
elif nota >= 80:
    letra = "B"
    descripcion = "Bien"
elif nota >= 70:
    letra = "C"
    descripcion = "Satisfactorio"
elif nota >= 60:
    letra = "D"
    descripcion = "Suficiente"
else:
    letra = "F"
    descripcion = "Reprobado"

print(f"\nNota: {nota} → Letra: {letra} ({descripcion})")
