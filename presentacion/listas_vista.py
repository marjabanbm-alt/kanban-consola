"""Vista CRUD de listas (columnas) dentro de un tablero."""
from auxiliares import mensajes as m
from negocio import lista_servicio

from . import consola, selectores, tablas


def listar(tablero) -> None:
    listas = lista_servicio.listar_listas(tablero.id)
    tablas.mostrar_listas(listas) if listas else consola.info(m.SIN_RESULTADOS)


def buscar(tablero) -> None:
    texto = consola.pedir_texto("Texto a buscar")
    listas = lista_servicio.buscar_listas(tablero.id, texto)
    tablas.mostrar_listas(listas) if listas else consola.info(m.SIN_RESULTADOS)


def crear(tablero) -> None:
    titulo = consola.pedir_texto("Título de la lista")
    lista = lista_servicio.crear_lista(tablero.id, titulo)
    consola.ok(f"{m.LISTA_CREADA} (ID {lista.id})")


def modificar(tablero) -> None:
    lista = selectores.seleccionar_lista(tablero)
    if lista is None:
        return
    titulo = consola.pedir_texto("Título", defecto=lista.titulo)
    posicion = consola.pedir_entero("Posición", defecto=lista.posicion, minimo=1)
    lista_servicio.modificar_lista(lista.id, titulo, posicion)
    consola.ok(m.LISTA_MODIFICADA)


def eliminar(tablero) -> None:
    lista = selectores.seleccionar_lista(tablero)
    if lista is None:
        return
    if consola.confirmar(f"¿Eliminar la lista '{lista.titulo}' y todas sus tarjetas?"):
        lista_servicio.eliminar_lista(lista.id)
        consola.ok(m.LISTA_ELIMINADA)
    else:
        consola.info(m.OPERACION_CANCELADA)


def abrir_menu() -> None:
    tablero = selectores.seleccionar_tablero()
    if tablero is None:
        return
    consola.correr_menu(
        f"LISTAS - Tablero: {tablero.titulo}",
        [
            ("1", "Listar listas", lambda: listar(tablero)),
            ("2", "Buscar listas", lambda: buscar(tablero)),
            ("3", "Crear lista", lambda: crear(tablero)),
            ("4", "Modificar lista", lambda: modificar(tablero)),
            ("5", "Eliminar lista", lambda: eliminar(tablero)),
        ],
    )
