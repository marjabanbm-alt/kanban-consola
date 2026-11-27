"""Repositorio de Lista."""
from peewee import fn

from datos.modelos.lista import Lista


def guardar(lista: Lista) -> Lista:
    lista.save()
    return lista


def listar_por_tablero(tablero_id: int) -> list:
    return list(
        Lista.select()
        .where(Lista.tablero == tablero_id)
        .order_by(Lista.posicion, Lista.id)
    )


def buscar_por_id(lista_id: int):
    return Lista.get_or_none(Lista.id == lista_id)


def buscar_por_titulo(tablero_id: int, texto: str) -> list:
    return list(
        Lista.select()
        .where((Lista.tablero == tablero_id) & Lista.titulo.contains(texto))
        .order_by(Lista.posicion, Lista.id)
    )


def siguiente_posicion(tablero_id: int) -> int:
    maxima = Lista.select(fn.MAX(Lista.posicion)).where(Lista.tablero == tablero_id).scalar()
    return 1 if maxima is None else maxima + 1


def eliminar(lista: Lista) -> int:
    """Elimina la lista y, en cascada, sus tarjetas."""
    return lista.delete_instance(recursive=True)
