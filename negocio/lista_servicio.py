"""Reglas de negocio de listas (columnas de un tablero)."""
from auxiliares import mensajes as m
from auxiliares import validaciones as v
from auxiliares.excepciones import ErrorNegocio
from datos.modelos.lista import Lista
from datos.repositorio import lista_repositorio as repo

from . import tablero_servicio


def obtener_lista(lista_id: int) -> Lista:
    lista = repo.buscar_por_id(lista_id)
    if lista is None:
        raise ErrorNegocio(m.LISTA_NO_ENCONTRADA)
    tablero_servicio.obtener_tablero(lista.tablero_id)  # valida permisos
    return lista


def listar_listas(tablero_id: int) -> list:
    tablero = tablero_servicio.obtener_tablero(tablero_id)
    return repo.listar_por_tablero(tablero.id)


def buscar_listas(tablero_id: int, texto: str) -> list:
    tablero = tablero_servicio.obtener_tablero(tablero_id)
    return repo.buscar_por_titulo(tablero.id, (texto or "").strip())


def crear_lista(tablero_id: int, titulo) -> Lista:
    tablero = tablero_servicio.obtener_tablero(tablero_id)
    lista = Lista(
        titulo=v.texto_obligatorio(titulo, "título"),
        posicion=repo.siguiente_posicion(tablero.id),
        tablero=tablero.id,
    )
    return repo.guardar(lista)


def modificar_lista(lista_id: int, titulo, posicion) -> Lista:
    lista = obtener_lista(lista_id)
    lista.titulo = v.texto_obligatorio(titulo, "título")
    lista.posicion = v.entero(posicion, minimo=1)
    return repo.guardar(lista)


def eliminar_lista(lista_id: int) -> None:
    repo.eliminar(obtener_lista(lista_id))
