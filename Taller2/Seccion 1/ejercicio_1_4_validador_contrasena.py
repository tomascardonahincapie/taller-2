
contrasena = input("Ingresa tu contraseña: ")

caracteres_especiales = "!@#$%^&*"
errores = []

if len(contrasena) < 8:
    errores.append("❌ Debe tener al menos 8 caracteres.")

tiene_mayuscula = False
for c in contrasena:
    if c.isupper():
        tiene_mayuscula = True
        break
if not tiene_mayuscula:
    errores.append("❌ Debe contener al menos una letra mayúscula.")

tiene_numero = False
for c in contrasena:
    if c.isdigit():
        tiene_numero = True
        break
if not tiene_numero:
    errores.append("❌ Debe contener al menos un número.")

tiene_especial = False
for c in contrasena:
    if c in caracteres_especiales:
        tiene_especial = True
        break
if not tiene_especial:
    errores.append(f"❌ Debe contener al menos un carácter especial ({caracteres_especiales}).")

if len(errores) == 0:
    print("\n✅ La contraseña es segura.")
else:
    print("\nLa contraseña no cumple con los siguientes criterios:")
    for error in errores:
        print(error)
