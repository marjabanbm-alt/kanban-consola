"""Vista CRUD de tarjetas dentro de un tablero."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from negocio import tarjeta_servicio, usuario_servicio

from . import consola, selectores, tablas


def _mostrar(tarjetas) -> None:
    tablas.mostrar_tarjetas(tarjetas) if tarjetas else consola.info(m.SIN_RESULTADOS)


def _pedir_asignado(actual_id=None):
    """Muestra los usuarios activos y pide el ID. ENTER conserva; '-' quita la asignación."""
    tablas.mostrar_usuarios_basico(usuario_servicio.listar_usuarios_activos())
    pista = "mantener actual" if actual_id else "sin asignar"
    texto = input(f"ID del usuario asignado (ENTER = {pista}, '-' = ninguno): ").strip()
    if not texto:
        return actual_id
    return None if texto == "-" else texto


def listar(tablero) -> None:
    _mostrar(tarjeta_servicio.listar_tarjetas_de_tablero(tablero.id))


def listar_por_lista(tablero) -> None:
    lista = selectores.seleccionar_lista(tablero)
    if lista is not None:
        _mostrar(tarjeta_servicio.listar_tarjetas_de_lista(lista.id))


def buscar(tablero) -> None:
    texto = consola.pedir_texto("Texto a buscar (título o descripción)")
    _mostrar(tarjeta_servicio.buscar_tarjetas(tablero.id, texto))


def ver_detalle(tablero) -> None:
    tarjeta = selectores.seleccionar_tarjeta(tablero)
    if tarjeta is not None:
        tablas.mostrar_detalle_tarjeta(tarjeta)


def crear(tablero) -> None:
    lista = selectores.seleccionar_lista(tablero)
    if lista is None:
        return
    titulo = consola.pedir_texto("Título de la tarjeta")
    descripcion = consola.pedir_texto("Descripción (opcional)", obligatorio=False)
    fecha = consola.pedir_fecha("Fecha límite (opcional)")
    prioridad = consola.pedir_opcion("Prioridad", c.PRIORIDADES, c.PRIORIDAD_POR_DEFECTO)
    asignado = _pedir_asignado()
    tarjeta = tarjeta_servicio.crear_tarjeta(
        lista.id, titulo, descripcion, fecha, prioridad, asignado
    )
    consola.ok(f"{m.TARJETA_CREADA} (ID {tarjeta.id})")


def modificar(tablero) -> None:
    tarjeta = selectores.seleccionar_tarjeta(tablero)
    if tarjeta is None:
        return
    titulo = consola.pedir_texto("Título", defecto=tarjeta.titulo)
    descripcion = consola.pedir_texto(
        "Descripción", defecto=tarjeta.descripcion or "", obligatorio=False
    )
    fecha = consola.pedir_fecha("Fecha límite", defecto=tarjeta.fecha_limite)
    prioridad = consola.pedir_opcion("Prioridad", c.PRIORIDADES, tarjeta.prioridad)
    asignado = _pedir_asignado(tarjeta.asignado_a_id)
    tarjeta_servicio.modificar_tarjeta(tarjeta.id, titulo, descripcion, fecha, prioridad, asignado)
    consola.ok(m.TARJETA_MODIFICADA)


def mover(tablero) -> None:
    tarjeta = selectores.seleccionar_tarjeta(tablero)
    if tarjeta is None:
        return
    consola.info("Seleccione la lista de destino:")
    destino = selectores.seleccionar_lista(tablero)
    if destino is None:
        return
    tarjeta_servicio.mover_tarjeta(tarjeta.id, destino.id)
    consola.ok(m.TARJETA_MOVIDA)


def eliminar(tablero) -> None:
    tarjeta = selectores.seleccionar_tarjeta(tablero)
    if tarjeta is None:
        return
    if consola.confirmar(f"¿Eliminar la tarjeta '{tarjeta.titulo}'?"):
        tarjeta_servicio.eliminar_tarjeta(tarjeta.id)
        consola.ok(m.TARJETA_ELIMINADA)
    else:
        consola.info(m.OPERACION_CANCELADA)


def mis_tarjetas() -> None:
    _mostrar(tarjeta_servicio.mis_tarjetas())


def abrir_menu() -> None:
    tablero = selectores.seleccionar_tablero()
    if tablero is None:
        return
    consola.correr_menu(
        f"TARJETAS - Tablero: {tablero.titulo}",
        [
            ("1", "Listar tarjetas del tablero", lambda: listar(tablero)),
            ("2", "Listar tarjetas de una lista", lambda: listar_por_lista(tablero)),
            ("3", "Ver detalle de una tarjeta", lambda: ver_detalle(tablero)),
            ("4", "Buscar tarjetas", lambda: buscar(tablero)),
            ("5", "Crear tarjeta", lambda: crear(tablero)),
            ("6", "Modificar tarjeta", lambda: modificar(tablero)),
            ("7", "Mover tarjeta a otra lista", lambda: mover(tablero)),
            ("8", "Eliminar tarjeta", lambda: eliminar(tablero)),
            ("9", "Mis tarjetas asignadas (todos los tableros)", mis_tarjetas),
        ],
    )
