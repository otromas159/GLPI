from collections import Counter
import re

from src.analytics.word_counter import STOPWORDS, NOMBRES


def limpiar_palabras(texto: str) -> list[str]:

    palabras = re.findall(
        r"\b[a-zA-ZáéíóúñÁÉÍÓÚÑ0-9]+\b",
        texto.lower()
    )

    resultado = []

    for palabra in palabras:

        if palabra.isdigit():
            continue

        if len(palabra) < 3:
            continue

        if len(palabra) > 30:
            continue

        if palabra in STOPWORDS:
            continue

        if palabra in NOMBRES:
            continue

        resultado.append(palabra)

    return resultado


def contar_bigramas(texto: str, contador: Counter):

    palabras = limpiar_palabras(texto)

    for i in range(len(palabras) - 1):

        bigrama = f"{palabras[i]} {palabras[i+1]}"

        contador[bigrama] += 1


def contar_trigramas(texto: str, contador: Counter):

    palabras = limpiar_palabras(texto)

    for i in range(len(palabras) - 2):

        trigrama = f"{palabras[i]} {palabras[i+1]} {palabras[i+2]}"

        contador[trigrama] += 1