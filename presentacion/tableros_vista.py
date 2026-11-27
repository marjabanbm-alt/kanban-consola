"""Vista CRUD de tableros."""
from auxiliares import mensajes as m
from negocio import tablero_servicio

from . import consola, selectores, tablas


def listar() -> None:
    tableros = tablero_servicio.listar_tableros()
    tablas.mostrar_tableros(tableros) if tableros else consola.info(m.SIN_RESULTADOS)


def buscar() -> None:
    texto = consola.pedir_texto("Texto a buscar")
    tableros = tablero_servicio.buscar_tableros(texto)
    tablas.mostrar_tableros(tableros) if tableros else consola.info(m.SIN_RESULTADOS)


def crear() -> None:
    titulo = consola.pedir_texto("Título")
    descripcion = consola.pedir_texto("Descripción (opcional)", obligatorio=False)
    tablero = tablero_servicio.crear_tablero(titulo, descripcion)
    consola.ok(f"{m.TABLERO_CREADO} (ID {tablero.id})")


def modificar() -> None:
    tablero = selectores.seleccionar_tablero()
    if tablero is None:
        return
    titulo = consola.pedir_texto("Título", defecto=tablero.titulo)
    descripcion = consola.pedir_texto(
        "Descripción", defecto=tablero.descripcion or "", obligatorio=False
    )
    tablero_servicio.modificar_tablero(tablero.id, titulo, descripcion)
    consola.ok(m.TABLERO_MODIFICADO)


def eliminar() -> None:
    tablero = selectores.seleccionar_tablero()
    if tablero is None:
        return
    if consola.confirmar(f"¿Eliminar '{tablero.titulo}' con todas sus listas y tarjetas?"):
        tablero_servicio.eliminar_tablero(tablero.id)
        consola.ok(m.TABLERO_ELIMINADO)
    else:
        consola.info(m.OPERACION_CANCELADA)


def ver_kanban() -> None:
    tablero = selectores.seleccionar_tablero()
    if tablero is None:
        return
    tablero, columnas = tablero_servicio.armar_vista_kanban(tablero.id)
    tablas.mostrar_kanban(tablero, columnas)


def abrir_menu() -> None:
    consola.correr_menu(
        "TABLEROS",
        [
            ("1", "Ver tablero (vista Kanban)", ver_kanban),
            ("2", "Listar tableros", listar),
            ("3", "Buscar tableros", buscar),
            ("4", "Crear tablero", crear),
            ("5", "Modificar tablero", modificar),
            ("6", "Eliminar tablero", eliminar),
        ],
    )
