import json
import os


def exportar_ticket(ticket, documento):

    carpeta = "output/tickets"

    os.makedirs(carpeta, exist_ok=True)

    ruta = os.path.join(
        carpeta,
        f"ticket_{ticket.id}.json"
    )

    datos = {
        "id": ticket.id,
        "titulo": ticket.titulo,
        "descripcion": ticket.descripcion,
        "seguimientos": ticket.seguimientos,
        "solucion": ticket.solucion,
        "documento": documento
    }

    with open(ruta, "w", encoding="utf-8") as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )