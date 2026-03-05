
while True:
    try:
        edad = int(input("Ingresa la edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        else:
            break
    except ValueError:
        print("Por favor ingresa un número entero válido.")

if edad <= 12:
    categoria = "niño"
elif edad <= 17:
    categoria = "adolescente"
elif edad <= 64:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"\nCon {edad} años, la persona es un/una: {categoria}.")
