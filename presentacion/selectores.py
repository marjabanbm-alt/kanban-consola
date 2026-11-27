"""Selección interactiva de registros por ID (siempre dentro de lo permitido al usuario)."""
from auxiliares import mensajes as m
from auxiliares.excepciones import ErrorNegocio
from negocio import lista_servicio, tablero_servicio, tarjeta_servicio, usuario_servicio

from . import consola, tablas


def _elegir(items, mostrar, prompt, vacio, no_encontrado):
    if not items:
        consola.info(vacio)
        return None
    mostrar(items)
    seleccionado = consola.pedir_entero(f"{prompt} (0 para cancelar)", minimo=0)
    if seleccionado == 0:
        consola.info(m.OPERACION_CANCELADA)
        return None
    for item in items:
        if item.id == seleccionado:
            return item
    raise ErrorNegocio(no_encontrado)


def seleccionar_tablero():
    return _elegir(
        tablero_servicio.listar_tableros(),
        tablas.mostrar_tableros,
        "ID del tablero",
        "No hay tableros. Cree uno primero.",
        m.TABLERO_NO_ENCONTRADO,
    )


def seleccionar_lista(tablero):
    return _elegir(
        lista_servicio.listar_listas(tablero.id),
        tablas.mostrar_listas,
        "ID de la lista",
        "El tablero no tiene listas. Cree una primero.",
        m.LISTA_NO_ENCONTRADA,
    )


def seleccionar_tarjeta(tablero):
    return _elegir(
        tarjeta_servicio.listar_tarjetas_de_tablero(tablero.id),
        tablas.mostrar_tarjetas,
        "ID de la tarjeta",
        "El tablero no tiene tarjetas.",
        m.TARJETA_NO_ENCONTRADA,
    )


def seleccionar_usuario():
    return _elegir(
        usuario_servicio.listar_usuarios(),
        tablas.mostrar_usuarios,
        "ID del usuario",
        m.SIN_RESULTADOS,
        m.USUARIO_NO_ENCONTRADO,
    )
