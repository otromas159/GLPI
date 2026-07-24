from dataclasses import dataclass, field


@dataclass
class KnowledgeCase:

    id: int

    categoria: str = ""

    subcategoria: str = ""

    software: list[str] = field(default_factory=list)

    hardware: list[str] = field(default_factory=list)

    servicios: list[str] = field(default_factory=list)

    problema: str = ""

    sintomas: list[str] = field(default_factory=list)

    causas_probables: list[str] = field(default_factory=list)

    acciones_realizadas: list[str] = field(default_factory=list)

    resultado: str = ""

    solucion: str = ""

    palabras_clave: list[str] = field(default_factory=list)

    relacionados: list[int] = field(default_factory=list)