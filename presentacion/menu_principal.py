"""Menú principal (solo accesible con sesión iniciada)."""
from auxiliares import mensajes as m
from negocio import auth_servicio, sesion

from . import (
    consola,
    cuenta_vista,
    listas_vista,
    tableros_vista,
    tarjetas_vista,
    usuarios_vista,
)


def _opciones_disponibles():
    opciones = [
        ("Tableros", tableros_vista.abrir_menu),
        ("Listas", listas_vista.abrir_menu),
        ("Tarjetas", tarjetas_vista.abrir_menu),
    ]
    if sesion.es_admin():
        opciones.append(("Usuarios", usuarios_vista.abrir_menu))
    opciones.append(("Mi cuenta", cuenta_vista.abrir_menu))
    return opciones


def ejecutar() -> bool:
    """Muestra el menú principal.

    Devuelve True si el usuario cerró sesión (se vuelve al login)
    y False si eligió salir de la aplicación.
    """
    if not sesion.hay_sesion():  # protección: sin login no hay menú
        consola.error(m.NO_AUTENTICADO)
        return True

    while True:
        usuario = sesion.usuario_actual()
        opciones = _opciones_disponibles()
        numero_cerrar = len(opciones) + 1

        consola.titulo(f"MENÚ PRINCIPAL - {usuario.nombre_usuario} ({usuario.rol})")
        for numero, (texto, _) in enumerate(opciones, start=1):
            print(f"  {numero}. {texto}")
        print(f"  {numero_cerrar}. Cerrar sesión")
        print("  0. Salir de la aplicación")

        eleccion = input(m.SELECCIONE_OPCION).strip()
        if eleccion == "0":
            auth_servicio.cerrar_sesion()
            return False
        if eleccion == str(numero_cerrar):
            auth_servicio.cerrar_sesion()
            consola.ok(m.SESION_CERRADA)
            return True
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            consola.ejecutar_seguro(opciones[int(eleccion) - 1][1])
        else:
            consola.error(m.OPCION_INVALIDA)
