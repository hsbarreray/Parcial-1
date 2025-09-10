import re

texto = "Salut! En 2025, 20 danseurs dansent ensemble. Liste: chaussures, musique, scène. Le prix est de 83,40€. Les étoiles (★) brillent la nuit. 16 chats sautent, 15 chiens tournent. Le code #5566 est spécial. 19 jours de danse, 13 jours de repos. @tous dansent. Le número magique est 1222. Que feriez-vous avec 57,70€? La réponse est dans la liste: sauter, tourner, profiter. Dansez votre vie! 100 mots, 19 entiers, 3 decimales, 2 listas."

patron_palabras = r'[@#]?([^\W\d_]+(?:-[^\W\d_]+)*)'

patron_decimales = r'\b-?\d+[.,]\d+\b'

patron_enteros_sueltos = r'(?<![\d\.,])\b-?\d+\b(?![.,]\d)'

patron_listas_bloque = r'(?i)\b(?:lista|liste):\s*([^.]+)'

def extraer_listas_de_palabras(texto):
    bloques = re.findall(patron_listas_bloque, texto)
    listas = []
    for bloque in bloques:
        items = [i.strip() for i in bloque.split(',')]
        clean = []
        for it in items:
            palabras_it = re.findall(patron_palabras, it)
            if palabras_it:
                clean.append(' '.join(palabras_it))
        if clean:
            listas.append(clean)
    return listas

palabras = re.findall(patron_palabras, texto)
decimales = re.findall(patron_decimales, texto)

enteros = re.findall(patron_enteros_sueltos, texto)
for d in decimales:
    izq, der = d.split(',' if ',' in d else '.')
    enteros += [izq.lstrip('-'), der]

listas = extraer_listas_de_palabras(texto)

print()
print("Cantidad de enteros:", len(enteros))
print("Cantidad de decimales:", len(decimales))
print("Cantidad de palabras:", len(palabras))
print("Cantidad de listas:", len(listas))
print()
