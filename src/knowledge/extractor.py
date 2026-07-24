from dataclasses import dataclass, field

@dataclass
class KnowledgeDocument:

    ticket_id: int

    titulo: str

    problema: str

    diagnosticos: list[str] = field(default_factory=list)

    acciones: list[str] = field(default_factory=list)

    resultados: list[str] = field(default_factory=list)

    solucion: str = ""