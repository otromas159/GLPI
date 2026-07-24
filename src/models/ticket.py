from dataclasses import dataclass, field

@dataclass
class Ticket:

    id: int

    titulo: str

    descripcion: str

    solucion: str = ""

    seguimientos: list[str] = field(default_factory=list)