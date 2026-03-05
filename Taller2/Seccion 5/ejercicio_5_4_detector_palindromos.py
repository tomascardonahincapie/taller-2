
def es_palindromo(texto):
    """
    Verifica si el texto es un palíndromo.
    Ignora espacios, mayúsculas y signos de puntuación.
    """
    signos = ".,;:!?¡¿-_()[]{}'\""

    limpio = ""
    for c in texto.lower():
        if c != " " and c not in signos:
            limpio += c

    reverso = limpio[::-1]
    return limpio == reverso

texto = input("Ingresa un texto para verificar si es palíndromo: ")

if es_palindromo(texto):
    print(f"\n✅ '{texto}' SÍ es un palíndromo.")
else:
    print(f"\n❌ '{texto}' NO es un palíndromo.")
