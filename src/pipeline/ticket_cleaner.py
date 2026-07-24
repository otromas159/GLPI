from src.cleaner.html_cleanner import limpiar_html


def limpiar_ticket(ticket):

    ticket.descripcion = limpiar_html(ticket.descripcion)

    ticket.solucion = limpiar_html(ticket.solucion)

    ticket.seguimientos = [
        limpiar_html(s)
        for s in ticket.seguimientos
    ]

    return ticket