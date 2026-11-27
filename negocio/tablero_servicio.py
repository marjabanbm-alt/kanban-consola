"""Reglas de negocio de tableros."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares import validaciones as v
from auxiliares.excepciones import ErrorNegocio
from datos.modelos.tablero import Tablero
from datos.repositorio import lista_repositorio as listas
from datos.repositorio import tablero_repositorio as repo
from datos.repositorio import tarjeta_repositorio as tarjetas

from . import sesion


def obtener_tablero(tablero_id: int) -> Tablero:
    """Devuelve el tablero si existe y el usuario es su propietario o administrador."""
    usuario = sesion.exigir_sesion()
    tablero = repo.buscar_por_id(tablero_id)
    if tablero is None:
        raise ErrorNegocio(m.TABLERO_NO_ENCONTRADO)
    if usuario.rol != c.ROL_ADMIN and tablero.propietario_id != usuario.id:
        raise ErrorNegocio(m.SIN_PERMISO)
    return tablero


def listar_tableros() -> list:
    usuario = sesion.exigir_sesion()
    if usuario.rol == c.ROL_ADMIN:
        return repo.listar_todos()
    return repo.listar_por_propietario(usuario.id)


def buscar_tableros(texto: str) -> list:
    usuario = sesion.exigir_sesion()
    propietario = None if usuario.rol == c.ROL_ADMIN else usuario.id
    return repo.buscar_por_titulo((texto or "").strip(), propietario)


def crear_tablero(titulo, descripcion=None) -> Tablero:
    usuario = sesion.exigir_sesion()
    tablero = Tablero(
        titulo=v.texto_obligatorio(titulo, "título"),
        descripcion=v.texto_opcional(descripcion, "descripción"),
        propietario=usuario.id,
    )
    return repo.guardar(tablero)


def modificar_tablero(tablero_id: int, titulo, descripcion=None) -> Tablero:
    tablero = obtener_tablero(tablero_id)
    tablero.titulo = v.texto_obligatorio(titulo, "título")
    tablero.descripcion = v.texto_opcional(descripcion, "descripción")
    return repo.guardar(tablero)


def eliminar_tablero(tablero_id: int) -> None:
    repo.eliminar(obtener_tablero(tablero_id))


def armar_vista_kanban(tablero_id: int):
    """Devuelve (tablero, [(lista, [tarjetas]), ...]) para mostrar el tablero completo."""
    tablero = obtener_tablero(tablero_id)
    columnas = [
        (lista, tarjetas.listar_por_lista(lista.id))
        for lista in listas.listar_por_tablero(tablero.id)
    ]
    return tablero, columnas
