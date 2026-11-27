"""Vista CRUD de usuarios (solo administradores)."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from negocio import usuario_servicio

from . import consola, selectores, tablas


def listar() -> None:
    usuarios = usuario_servicio.listar_usuarios()
    tablas.mostrar_usuarios(usuarios) if usuarios else consola.info(m.SIN_RESULTADOS)


def buscar() -> None:
    texto = consola.pedir_texto("Texto a buscar (usuario, nombre o email)")
    usuarios = usuario_servicio.buscar_usuarios(texto)
    tablas.mostrar_usuarios(usuarios) if usuarios else consola.info(m.SIN_RESULTADOS)


def crear() -> None:
    nombre_usuario = consola.pedir_texto("Nombre de usuario")
    nombre_completo = consola.pedir_texto("Nombre completo")
    email = consola.pedir_texto("Email")
    rol = consola.pedir_opcion("Rol", c.ROLES, c.ROL_USUARIO)
    password = consola.pedir_password_nueva("Contraseña")
    if password is None:
        return
    usuario_servicio.crear_usuario(nombre_usuario, nombre_completo, email, password, rol)
    consola.ok(m.USUARIO_CREADO.format(valor=nombre_usuario.lower()))


def modificar() -> None:
    usuario = selectores.seleccionar_usuario()
    if usuario is None:
        return
    nombre_completo = consola.pedir_texto("Nombre completo", defecto=usuario.nombre_completo)
    email = consola.pedir_texto("Email", defecto=usuario.email)
    rol = consola.pedir_opcion("Rol", c.ROLES, usuario.rol)
    usuario_servicio.modificar_usuario(usuario.id, nombre_completo, email, rol)
    consola.ok(m.USUARIO_MODIFICADO)


def deshabilitar() -> None:
    usuario = selectores.seleccionar_usuario()
    if usuario is None:
        return
    if consola.confirmar(f"¿Deshabilitar al usuario '{usuario.nombre_usuario}'?"):
        usuario_servicio.deshabilitar_usuario(usuario.id)
        consola.ok(m.USUARIO_DESHABILITADO_OK)
    else:
        consola.info(m.OPERACION_CANCELADA)


def habilitar() -> None:
    usuario = selectores.seleccionar_usuario()
    if usuario is None:
        return
    usuario_servicio.habilitar_usuario(usuario.id)
    consola.ok(m.USUARIO_HABILITADO_OK)


def restablecer_password() -> None:
    usuario = selectores.seleccionar_usuario()
    if usuario is None:
        return
    nueva = consola.pedir_password_nueva(f"Nueva contraseña para '{usuario.nombre_usuario}'")
    if nueva is None:
        return
    usuario_servicio.restablecer_password(usuario.id, nueva)
    consola.ok(m.PASSWORD_CAMBIADA)


def abrir_menu() -> None:
    consola.correr_menu(
        "USUARIOS",
        [
            ("1", "Listar usuarios", listar),
            ("2", "Buscar usuarios", buscar),
            ("3", "Crear usuario", crear),
            ("4", "Modificar usuario", modificar),
            ("5", "Deshabilitar usuario", deshabilitar),
            ("6", "Habilitar usuario", habilitar),
            ("7", "Restablecer contraseña de un usuario", restablecer_password),
        ],
    )
