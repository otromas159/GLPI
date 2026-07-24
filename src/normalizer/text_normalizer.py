import re

SALUDOS = [

    "buenos días",
    "buen dia",
    "buenas tardes",
    "buenas noches",
    "cordial saludo",
    "hola",
    "gracias",
    "quedo atento",
    "quedo atenta",
    "saludos",
]

def normalizar_texto(texto: str) -> str:

    lineas = texto.split("\n")

    resultado = []

    for linea in lineas:

        linea = linea.strip()

        if not linea:
            continue

        minuscula = linea.lower()

        eliminar = False

        for saludo in SALUDOS:

            if minuscula.startswith(saludo):

                eliminar = True
                break

        if not eliminar:

            resultado.append(linea)

    return "\n".join(resultado)