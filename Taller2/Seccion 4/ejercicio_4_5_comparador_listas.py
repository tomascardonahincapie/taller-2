
def ingresar_lista(nombre):
    entrada = input(f"Ingresa los elementos de la {nombre} separados por comas: ")
    return [e.strip() for e in entrada.split(",") if e.strip()]

lista1 = ingresar_lista("lista 1")
lista2 = ingresar_lista("lista 2")

comunes = []
for elem in lista1:
    esta_en_lista2 = False
    for e2 in lista2:
        if elem == e2:
            esta_en_lista2 = True
            break
    esta_en_comunes = False
    for c in comunes:
        if c == elem:
            esta_en_comunes = True
            break
    if esta_en_lista2 and not esta_en_comunes:
        comunes.append(elem)

unicos_lista1 = []
for elem in lista1:
    esta_en_lista2 = False
    for e2 in lista2:
        if elem == e2:
            esta_en_lista2 = True
            break
    if not esta_en_lista2:
        esta_en_unicos = False
        for u in unicos_lista1:
            if u == elem:
                esta_en_unicos = True
                break
        if not esta_en_unicos:
            unicos_lista1.append(elem)

unicos_lista2 = []
for elem in lista2:
    esta_en_lista1 = False
    for e1 in lista1:
        if elem == e1:
            esta_en_lista1 = True
            break
    if not esta_en_lista1:
        esta_en_unicos = False
        for u in unicos_lista2:
            if u == elem:
                esta_en_unicos = True
                break
        if not esta_en_unicos:
            unicos_lista2.append(elem)

print(f"\nLista 1:          {lista1}")
print(f"Lista 2:          {lista2}")
print(f"Comunes:          {comunes}")
print(f"Únicos lista 1:   {unicos_lista1}")
print(f"Únicos lista 2:   {unicos_lista2}")
