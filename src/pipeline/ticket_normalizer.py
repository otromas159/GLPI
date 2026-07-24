from src.normalizer.text_normalizer import normalizar_texto


def normalizar_ticket(ticket):

    ticket.descripcion = normalizar_texto(ticket.descripcion)

    ticket.solucion = normalizar_texto(ticket.solucion)

    ticket.seguimientos = [
    texto
    for texto in (
        normalizar_texto(s)
        for s in ticket.seguimientos
    )
    if texto.strip()
]

    return ticket