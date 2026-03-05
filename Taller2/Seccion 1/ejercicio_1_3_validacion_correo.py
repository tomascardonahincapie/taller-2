

correo = input("Ingresa tu correo electrónico: ")

es_valido = True
mensaje = ""

if "@" not in correo:
    es_valido = False
    mensaje = "El correo debe contener '@'."
else:
    partes = correo.split("@")
    if len(partes) != 2 or partes[0] == "" or partes[1] == "":
        es_valido = False
        mensaje = "El formato del correo no es válido."
    elif "." not in partes[1]:
        es_valido = False
        mensaje = "El dominio debe contener '.'."
    elif partes[1].startswith(".") or partes[1].endswith("."):
        es_valido = False
        mensaje = "El punto no puede estar al inicio o al final del dominio."

if es_valido:
    print(f"\n✅ El correo '{correo}' es válido.")
else:
    print(f"\n❌ Correo no válido: {mensaje}")
