"""Repositorio de Tablero."""
from datos.modelos.tablero import Tablero


def guardar(tablero: Tablero) -> Tablero:
    tablero.save()
    return tablero


def listar_todos() -> list:
    return list(Tablero.select().order_by(Tablero.id))


def listar_por_propietario(usuario_id: int) -> list:
    return list(
        Tablero.select().where(Tablero.propietario == usuario_id).order_by(Tablero.id)
    )


def buscar_por_id(tablero_id: int):
    return Tablero.get_or_none(Tablero.id == tablero_id)


def buscar_por_titulo(texto: str, propietario_id=None) -> list:
    condicion = Tablero.titulo.contains(texto) | Tablero.descripcion.contains(texto)
    if propietario_id is not None:
        condicion = condicion & (Tablero.propietario == propietario_id)
    return list(Tablero.select().where(condicion).order_by(Tablero.id))


def eliminar(tablero: Tablero) -> int:
    """Elimina el tablero y, en cascada, sus listas y tarjetas."""
    return tablero.delete_instance(recursive=True)
