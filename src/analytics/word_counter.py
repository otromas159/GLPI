from collections import Counter
import re

STOPWORDS = {
    "de", "la", "el", "los", "las",
    "un", "una", "unos", "unas",
    "para", "por", "con", "sin",
    "del", "al",
    "que", "como",
    "se", "es", "en", "y", "o",
    "a", "su", "sus",

    "buenos", "buenas",
    "dias", "día", "días",
    "favor",
    "gracias",
    "cordial",
    "saludo",
    "atento",
    "quedo",
    "hola",
    "adjunto",
    "verificar",

    "caso",
    "casos",
    "este",
    "esta",
    "esto",
    "pero",
    "nos",
    "fue",
    "cuando",
    "solo",
    "muy",
    "hacer",
    "puede",
    "tema",
    "forma",
    "todos",
    "desde",
    "porque",
    "sobre",
    "mismo",
    "ser",
    "más",
    "nuevamente"
}

NOMBRES = {
    "daniel",
    "paola",
    "emilse",
    "ruby",
    "henry",
    "wilson",
    "monica",
    "sandra"
}


def contar_palabras(texto, contador):

    palabras = re.findall(
        r"\b[a-zA-ZáéíóúñÁÉÍÓÚÑ0-9]+\b",
        texto.lower()
    )

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

        contador[palabra] += 1