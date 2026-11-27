"""Repositorio de Tarjeta."""
from peewee import fn

from datos.modelos.lista import Lista
from datos.modelos.tarjeta import Tarjeta


def guardar(tarjeta: Tarjeta) -> Tarjeta:
    tarjeta.save()
    return tarjeta


def listar_por_lista(lista_id: int) -> list:
    return list(
        Tarjeta.select()
        .where(Tarjeta.lista == lista_id)
        .order_by(Tarjeta.posicion, Tarjeta.id)
    )


def listar_por_tablero(tablero_id: int) -> list:
    return list(
        Tarjeta.select()
        .join(Lista)
        .where(Lista.tablero == tablero_id)
        .order_by(Lista.posicion, Tarjeta.posicion, Tarjeta.id)
    )


def listar_por_asignado(usuario_id: int) -> list:
    return list(
        Tarjeta.select()
        .where(Tarjeta.asignado_a == usuario_id)
        .order_by(Tarjeta.fecha_limite, Tarjeta.id)
    )


def buscar_por_id(tarjeta_id: int):
    return Tarjeta.get_or_none(Tarjeta.id == tarjeta_id)


def buscar_por_texto(tablero_id: int, texto: str) -> list:
    return list(
        Tarjeta.select()
        .join(Lista)
        .where(
            (Lista.tablero == tablero_id)
            & (Tarjeta.titulo.contains(texto) | Tarjeta.descripcion.contains(texto))
        )
        .order_by(Lista.posicion, Tarjeta.posicion, Tarjeta.id)
    )


def siguiente_posicion(lista_id: int) -> int:
    maxima = Tarjeta.select(fn.MAX(Tarjeta.posicion)).where(Tarjeta.lista == lista_id).scalar()
    return 1 if maxima is None else maxima + 1


def eliminar(tarjeta: Tarjeta) -> int:
    return tarjeta.delete_instance()
