"""Autenticación: login y logout."""
from auxiliares import mensajes as m
from auxiliares.excepciones import ErrorNegocio
from datos.repositorio import usuario_repositorio as usuarios

from . import sesion
from .seguridad import verificar_password


def iniciar_sesion(nombre_usuario: str, password: str):
    """Valida credenciales y abre la sesión. Lanza ErrorNegocio si fallan."""
    nombre = (nombre_usuario or "").strip().lower()
    usuario = usuarios.buscar_por_nombre_usuario(nombre)

    # Mismo mensaje para usuario inexistente y contraseña incorrecta
    if usuario is None or not verificar_password(password or "", usuario.password_hash):
        raise ErrorNegocio(m.CREDENCIALES_INVALIDAS)
    if not usuario.activo:
        raise ErrorNegocio(m.USUARIO_DESHABILITADO)

    sesion.iniciar(usuario)
    return usuario


def cerrar_sesion() -> None:
    sesion.cerrar()
