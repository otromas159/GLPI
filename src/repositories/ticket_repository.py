from src.database.connection import obtener_conexion
from src.models.ticket import Ticket


def obtener_todos_los_tickets():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            content
        FROM glpi_tickets
        WHERE is_deleted = 0
        ORDER BY id
    """)

    for fila in cursor:

        yield Ticket(
            id=fila[0],
            titulo=fila[1],
            descripcion=fila[2]
        )

    cursor.close()
    conexion.close()