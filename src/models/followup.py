from dataclasses import dataclass

@dataclass
class FollowUp:
    contenido: str
    fecha: str | None = None
    usuario: str | None = None
    privado: bool = False