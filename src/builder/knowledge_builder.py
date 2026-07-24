from models.knowledgeCase import Knowledge

from src.enrichers.software_enricher import enriquecer_software
from src.extractors.action_extractor import extraer_acciones

from src.classifier.ticket_classifier import clasificar


def construir_conocimiento(ticket):

    return Knowledge(

        id=ticket.id,

        categoria=clasificar(ticket),
        
        knowledge = enriquecer_software(knowledge),

        acciones=extraer_acciones(ticket),

        problema=ticket.descripcion,

        solucion=ticket.solucion

    )