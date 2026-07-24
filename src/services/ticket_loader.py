from src.repositories.ticket_repository import obtener_todos_los_tickets
from src.repositories.solution_repository import obtener_solucion
from src.repositories.followup_repository import obtener_seguimientos


def cargar_todos():

    for ticket in obtener_todos_los_tickets():

        ticket.solucion = obtener_solucion(ticket.id)

        ticket.seguimientos = obtener_seguimientos(ticket.id)

        yield ticket