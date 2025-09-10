import re

texto = "Ciao! Nel 2025, 21 ballerini danzano insieme. Lista: scarpe, musica, palco. Il prezzo è €80,80. Le stelle (★) brillano sopra il palco. 15 gatti saltano, 14 cani girano. Il codice #7788 è speciale. 18 giorni di danza, 14 di riposo. @tutti danzano. Il numero magico è 1232. Cosa faresti con 57,90€? La risposta è nella lista: saltare, girare, godere. Danza la tua vita! 100 parole, 18 interi, 3 decimales, 2 listas."

patron_palabras = r'[@#]?([^\W\d_]+(?:-[^\W\d_]+)*)'

patron_decimales = r'\b-?\d+[.,]\d+\b'

patron_enteros_sueltos = r'(?<![\d\.,])\b-?\d+\b(?![.,]\d)'

patron_listas_bloque = r'(?i)\b(?:liste|lista):\s*([^.]+)'

def extraer_listas_de_palabras(texto):
    bloques = re.findall(patron_listas_bloque, texto)
    listas = []
    for bloque in bloques:
        items = [i.strip() for i in bloque.split(',')]
        limpios = []
        for it in items:
            palabras_it = re.findall(patron_palabras, it)
            if palabras_it:
                limpios.append(' '.join(palabras_it))
        if limpios:
            listas.append(limpios)
    return listas

def analizar(texto):
    palabras = re.findall(patron_palabras, texto)

    decimales = re.findall(patron_decimales, texto)

    enteros = re.findall(patron_enteros_sueltos, texto)
    for d in decimales:
        sep = ',' if ',' in d else '.'
        izq, der = d.split(sep, 1)
        enteros += [izq.lstrip('-'), der]

    listas = extraer_listas_de_palabras(texto)

    return palabras, enteros, decimales, listas

enteros = re.findall(patron_enteros_sueltos, texto)
decimales = re.findall(patron_decimales, texto)
palabras = re.findall(patron_palabras, texto)
listas = extraer_listas_de_palabras(texto)

print()
print("Cantidad de enteros:", len(enteros))
print("Cantidad de decimales:", len(decimales))
print("Cantidad de palabras:", len(palabras))
print("Cantidad de listas:", len(listas))
print()
