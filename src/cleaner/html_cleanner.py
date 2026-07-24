import html
from bs4 import BeautifulSoup


def limpiar_html(texto: str) -> str:

    if not texto:
        return ""

    # Convierte &lt; en <
    texto = html.unescape(texto)

    # Elimina etiquetas
    soup = BeautifulSoup(texto, "html.parser")

    texto = soup.get_text(separator="\n")

    # Quitar espacios repetidos
    lineas = []

    for linea in texto.splitlines():

        linea = linea.strip()

        if linea:

            lineas.append(linea)

    return "\n".join(lineas)