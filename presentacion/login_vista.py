"""Pantalla de inicio de sesión."""
from auxiliares import configuracion as cfg
from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares.excepciones import ErrorNegocio
from negocio import auth_servicio

from . import consola


def pantalla_login() -> bool:
    """Pide credenciales. Devuelve True si el login fue exitoso, False si se debe salir."""
    consola.titulo(f"{cfg.NOMBRE_APP} - INICIAR SESIÓN")
    consola.info(m.LOGIN_INSTRUCCION)

    for intento in range(1, c.MAX_INTENTOS_LOGIN + 1):
        nombre = input("Usuario: ").strip()
        if nombre.lower() == "salir":
            return False
        password = consola.pedir_password("Contraseña")
        try:
            usuario = auth_servicio.iniciar_sesion(nombre, password)
        except ErrorNegocio as exc:
            consola.error(f"{exc} (intento {intento}/{c.MAX_INTENTOS_LOGIN})")
            continue
        consola.ok(m.LOGIN_BIENVENIDA.format(nombre=usuario.nombre_completo))
        return True

    consola.error(m.LOGIN_BLOQUEADO)
    return False
