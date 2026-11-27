"""Repositorio de Usuario (funciones de acceso a datos)."""
from auxiliares.constantes import ROL_ADMIN
from datos.modelos.usuario import Usuario


def guardar(usuario: Usuario) -> Usuario:
    usuario.save()
    return usuario


def listar(solo_activos: bool = False) -> list:
    consulta = Usuario.select().order_by(Usuario.nombre_usuario)
    if solo_activos:
        consulta = consulta.where(Usuario.activo == True)  # noqa: E712
    return list(consulta)


def buscar_por_id(usuario_id: int):
    return Usuario.get_or_none(Usuario.id == usuario_id)


def buscar_por_nombre_usuario(nombre_usuario: str):
    return Usuario.get_or_none(Usuario.nombre_usuario == nombre_usuario)


def buscar_por_email(email: str):
    return Usuario.get_or_none(Usuario.email == email)


def buscar_por_texto(texto: str) -> list:
    consulta = (
        Usuario.select()
        .where(
            Usuario.nombre_usuario.contains(texto)
            | Usuario.nombre_completo.contains(texto)
            | Usuario.email.contains(texto)
        )
        .order_by(Usuario.nombre_usuario)
    )
    return list(consulta)


def contar() -> int:
    return Usuario.select().count()


def contar_admins_activos() -> int:
    return (
        Usuario.select()
        .where((Usuario.rol == ROL_ADMIN) & (Usuario.activo == True))  # noqa: E712
        .count()
    )


def eliminar(usuario: Usuario) -> int:
    """Eliminación física (la aplicación usa deshabilitar; se deja disponible)."""
    return usuario.delete_instance()
