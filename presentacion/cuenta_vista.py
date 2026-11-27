"""Vista de 'Mi cuenta': datos propios y cambio de contraseña."""
from auxiliares import mensajes as m
from negocio import sesion, usuario_servicio

from . import consola, tablas


def ver_datos() -> None:
    tablas.mostrar_usuarios([sesion.exigir_sesion()])


def modificar_datos() -> None:
    usuario = sesion.exigir_sesion()
    nombre_completo = consola.pedir_texto("Nombre completo", defecto=usuario.nombre_completo)
    email = consola.pedir_texto("Email", defecto=usuario.email)
    usuario_servicio.modificar_mi_perfil(nombre_completo, email)
    consola.ok(m.USUARIO_MODIFICADO)


def cambiar_password() -> None:
    actual = consola.pedir_password("Contraseña actual")
    nueva = consola.pedir_password_nueva("Nueva contraseña")
    if nueva is None:
        return
    usuario_servicio.cambiar_mi_password(actual, nueva)
    consola.ok(m.PASSWORD_CAMBIADA)


def abrir_menu() -> None:
    consola.correr_menu(
        "MI CUENTA",
        [
            ("1", "Ver mis datos", ver_datos),
            ("2", "Modificar mis datos", modificar_datos),
            ("3", "Cambiar mi contraseña", cambiar_password),
        ],
    )
