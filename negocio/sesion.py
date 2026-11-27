"""Sesión de la aplicación: guarda el usuario autenticado."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares.excepciones import ErrorNegocio

_usuario_actual = None


def iniciar(usuario) -> None:
    global _usuario_actual
    _usuario_actual = usuario


def cerrar() -> None:
    global _usuario_actual
    _usuario_actual = None


def usuario_actual():
    return _usuario_actual


def hay_sesion() -> bool:
    return _usuario_actual is not None


def es_admin() -> bool:
    return hay_sesion() and _usuario_actual.rol == c.ROL_ADMIN


def exigir_sesion():
    """Devuelve el usuario autenticado o lanza ErrorNegocio si no hay sesión."""
    if _usuario_actual is None:
        raise ErrorNegocio(m.NO_AUTENTICADO)
    return _usuario_actual
