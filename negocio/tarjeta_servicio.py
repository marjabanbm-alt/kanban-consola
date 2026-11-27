"""Reglas de negocio de tarjetas."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares import validaciones as v
from auxiliares.excepciones import ErrorNegocio
from datos.modelos.tarjeta import Tarjeta
from datos.repositorio import tarjeta_repositorio as repo
from datos.repositorio import usuario_repositorio as usuarios

from . import lista_servicio, sesion, tablero_servicio


def _validar_asignado(usuario_id):
    """Devuelve el id del usuario asignado (o None) verificando que exista y esté activo."""
    if usuario_id in (None, ""):
        return None
    usuario = usuarios.buscar_por_id(v.entero(usuario_id, minimo=1))
    if usuario is None or not usuario.activo:
        raise ErrorNegocio(m.ASIGNADO_INVALIDO)
    return usuario.id


def obtener_tarjeta(tarjeta_id: int) -> Tarjeta:
    tarjeta = repo.buscar_por_id(tarjeta_id)
    if tarjeta is None:
        raise ErrorNegocio(m.TARJETA_NO_ENCONTRADA)
    lista_servicio.obtener_lista(tarjeta.lista_id)  # valida permisos
    return tarjeta


def listar_tarjetas_de_lista(lista_id: int) -> list:
    lista = lista_servicio.obtener_lista(lista_id)
    return repo.listar_por_lista(lista.id)


def listar_tarjetas_de_tablero(tablero_id: int) -> list:
    tablero = tablero_servicio.obtener_tablero(tablero_id)
    return repo.listar_por_tablero(tablero.id)


def buscar_tarjetas(tablero_id: int, texto: str) -> list:
    tablero = tablero_servicio.obtener_tablero(tablero_id)
    return repo.buscar_por_texto(tablero.id, (texto or "").strip())


def mis_tarjetas() -> list:
    usuario = sesion.exigir_sesion()
    return repo.listar_por_asignado(usuario.id)


def crear_tarjeta(
    lista_id: int,
    titulo,
    descripcion=None,
    fecha_limite=None,
    prioridad=c.PRIORIDAD_POR_DEFECTO,
    asignado_a_id=None,
) -> Tarjeta:
    lista = lista_servicio.obtener_lista(lista_id)
    tarjeta = Tarjeta(
        titulo=v.texto_obligatorio(titulo, "título"),
        descripcion=v.texto_opcional(descripcion, "descripción"),
        fecha_limite=v.fecha_opcional(fecha_limite),
        prioridad=v.prioridad(prioridad),
        posicion=repo.siguiente_posicion(lista.id),
        lista=lista.id,
        asignado_a=_validar_asignado(asignado_a_id),
    )
    return repo.guardar(tarjeta)


def modificar_tarjeta(
    tarjeta_id: int, titulo, descripcion, fecha_limite, prioridad, asignado_a_id
) -> Tarjeta:
    tarjeta = obtener_tarjeta(tarjeta_id)
    tarjeta.titulo = v.texto_obligatorio(titulo, "título")
    tarjeta.descripcion = v.texto_opcional(descripcion, "descripción")
    tarjeta.fecha_limite = v.fecha_opcional(fecha_limite)
    tarjeta.prioridad = v.prioridad(prioridad)
    tarjeta.asignado_a = _validar_asignado(asignado_a_id)
    return repo.guardar(tarjeta)


def mover_tarjeta(tarjeta_id: int, lista_destino_id: int) -> Tarjeta:
    """Mueve la tarjeta al final de otra lista del mismo tablero."""
    tarjeta = obtener_tarjeta(tarjeta_id)
    destino = lista_servicio.obtener_lista(lista_destino_id)
    if destino.tablero_id != tarjeta.lista.tablero_id:
        raise ErrorNegocio(m.LISTA_OTRO_TABLERO)
    tarjeta.lista = destino.id
    tarjeta.posicion = repo.siguiente_posicion(destino.id)
    return repo.guardar(tarjeta)


def eliminar_tarjeta(tarjeta_id: int) -> None:
    repo.eliminar(obtener_tarjeta(tarjeta_id))
