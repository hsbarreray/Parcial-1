import re

texto = "En el año 2025, 22 bailarines danzan juntos. ¡Hola! ¿Te gusta bailar? El cielo rítmico, las estrellas (★) brillan. 18 niños saltan, 17.50 horas de ensayo. Lista: zapatillas, música, escenario. El costo es $85.20. ¿Sabías que el código #3344 es especial? La vida es movimiento, @todos participan. El tiempo pasa, 19 días de espectáculo. ¡Baila! El número especial es 1212. ¿Qué harías con 54.90 pesos? La respuesta está en la lista: saltar, girar, disfrutar. ¡Baila tu vida! 100 palabras, 19 enteros, 3 decimales, 2 listas."

patron_enteros = r'(?<![\d.])\b-?\d+\b'

patron_decimales = r'\b-?\d+\.\d+\b'

patron_palabras = r'[@#]?([A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+(?:-[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+)*)'

patron_listas_bloque = r'(?i)\blista:\s*([^.]+)'

def extraer_listas_de_palabras(texto):
    bloques = re.findall(patron_listas_bloque, texto)
    listas = []
    for bloque in bloques:
        items = [i.strip() for i in bloque.split(',')]
        items_limpios = []
        for it in items:
            palabras_it = re.findall(patron_palabras, it)
            if palabras_it:
                items_limpios.append(' '.join(palabras_it))
        if items_limpios:
            listas.append(items_limpios)
    return listas

enteros = re.findall(patron_enteros, texto)
decimales = re.findall(patron_decimales, texto)
palabras = re.findall(patron_palabras, texto)
listas = extraer_listas_de_palabras(texto)

print()
print("Cantidad de enteros:", len(enteros))
print("Cantidad de decimales:", len(decimales))
print("Cantidad de palabras:", len(palabras))
print("Cantidad de listas:", len(listas))
print()