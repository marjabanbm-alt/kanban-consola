"""Reglas de negocio para la gestión de usuarios."""
from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares import validaciones as v
from auxiliares.excepciones import ErrorNegocio
from datos.modelos.usuario import Usuario
from datos.repositorio import usuario_repositorio as repo

from . import sesion
from .seguridad import hashear_password, verificar_password


# ---------- helpers internos ----------
def _exigir_admin():
    usuario = sesion.exigir_sesion()
    if usuario.rol != c.ROL_ADMIN:
        raise ErrorNegocio(m.SOLO_ADMIN)
    return usuario


def _obtener(usuario_id: int) -> Usuario:
    usuario = repo.buscar_por_id(usuario_id)
    if usuario is None:
        raise ErrorNegocio(m.USUARIO_NO_ENCONTRADO)
    return usuario


def _validar_email_unico(email: str, excluir_id=None) -> None:
    existente = repo.buscar_por_email(email)
    if existente is not None and existente.id != excluir_id:
        raise ErrorNegocio(m.EMAIL_DUPLICADO.format(valor=email))


def _refrescar_sesion(usuario: Usuario) -> None:
    actual = sesion.usuario_actual()
    if actual is not None and actual.id == usuario.id:
        sesion.iniciar(usuario)


def _es_ultimo_admin_activo(usuario: Usuario) -> bool:
    return (
        usuario.rol == c.ROL_ADMIN
        and usuario.activo
        and repo.contar_admins_activos() <= 1
    )


def _crear(nombre_usuario, nombre_completo, email, password, rol) -> Usuario:
    nombre_usuario = v.nombre_usuario(nombre_usuario)
    nombre_completo = v.texto_obligatorio(nombre_completo, "nombre completo", 100)
    email = v.email(email)
    password = v.password(password)
    rol = v.rol(rol)

    if repo.buscar_por_nombre_usuario(nombre_usuario) is not None:
        raise ErrorNegocio(m.USUARIO_DUPLICADO.format(valor=nombre_usuario))
    _validar_email_unico(email)

    usuario = Usuario(
        nombre_usuario=nombre_usuario,
        nombre_completo=nombre_completo,
        email=email,
        password_hash=hashear_password(password),
        rol=rol,
    )
    return repo.guardar(usuario)


# ---------- usuario inicial ----------
def crear_usuario_inicial() -> bool:
    """Crea el administrador inicial si no existe ningún usuario. Devuelve True si lo creó."""
    if repo.contar() > 0:
        return False
    _crear(
        c.ADMIN_INICIAL_USUARIO,
        c.ADMIN_INICIAL_NOMBRE,
        c.ADMIN_INICIAL_EMAIL,
        c.ADMIN_INICIAL_PASSWORD,
        c.ROL_ADMIN,
    )
    return True


# ---------- CRUD (solo administradores) ----------
def crear_usuario(nombre_usuario, nombre_completo, email, password, rol=c.ROL_USUARIO) -> Usuario:
    _exigir_admin()
    return _crear(nombre_usuario, nombre_completo, email, password, rol)


def listar_usuarios() -> list:
    _exigir_admin()
    return repo.listar()


def listar_usuarios_activos() -> list:
    sesion.exigir_sesion()
    return repo.listar(solo_activos=True)


def buscar_usuarios(texto: str) -> list:
    _exigir_admin()
    return repo.buscar_por_texto((texto or "").strip())


def obtener_usuario(usuario_id: int) -> Usuario:
    _exigir_admin()
    return _obtener(usuario_id)


def modificar_usuario(usuario_id: int, nombre_completo, email, rol) -> Usuario:
    _exigir_admin()
    usuario = _obtener(usuario_id)
    nombre_completo = v.texto_obligatorio(nombre_completo, "nombre completo", 100)
    email = v.email(email)
    rol = v.rol(rol)
    _validar_email_unico(email, excluir_id=usuario.id)

    if rol != c.ROL_ADMIN and _es_ultimo_admin_activo(usuario):
        raise ErrorNegocio(m.ULTIMO_ADMIN)

    usuario.nombre_completo = nombre_completo
    usuario.email = email
    usuario.rol = rol
    repo.guardar(usuario)
    _refrescar_sesion(usuario)
    return usuario


def deshabilitar_usuario(usuario_id: int) -> Usuario:
    actual = _exigir_admin()
    usuario = _obtener(usuario_id)
    if usuario.id == actual.id:
        raise ErrorNegocio(m.NO_DESHABILITAR_SELF)
    if not usuario.activo:
        raise ErrorNegocio(m.USUARIO_YA_DESHABILITADO)
    if _es_ultimo_admin_activo(usuario):
        raise ErrorNegocio(m.ULTIMO_ADMIN)
    usuario.activo = False
    return repo.guardar(usuario)


def habilitar_usuario(usuario_id: int) -> Usuario:
    _exigir_admin()
    usuario = _obtener(usuario_id)
    if usuario.activo:
        raise ErrorNegocio(m.USUARIO_YA_HABILITADO)
    usuario.activo = True
    return repo.guardar(usuario)


def restablecer_password(usuario_id: int, nueva_password: str) -> Usuario:
    """Un administrador define una nueva contraseña para otro usuario."""
    _exigir_admin()
    usuario = _obtener(usuario_id)
    usuario.password_hash = hashear_password(v.password(nueva_password))
    return repo.guardar(usuario)


# ---------- Mi cuenta (cualquier usuario autenticado) ----------
def modificar_mi_perfil(nombre_completo, email) -> Usuario:
    actual = sesion.exigir_sesion()
    usuario = _obtener(actual.id)
    usuario.nombre_completo = v.texto_obligatorio(nombre_completo, "nombre completo", 100)
    usuario.email = v.email(email)
    _validar_email_unico(usuario.email, excluir_id=usuario.id)
    repo.guardar(usuario)
    sesion.iniciar(usuario)  # actualiza la sesión
    return usuario


def cambiar_mi_password(password_actual: str, nueva_password: str) -> Usuario:
    actual = sesion.exigir_sesion()
    usuario = _obtener(actual.id)
    if not verificar_password(password_actual or "", usuario.password_hash):
        raise ErrorNegocio(m.PASSWORD_ACTUAL_INCORRECTA)
    usuario.password_hash = hashear_password(v.password(nueva_password))
    repo.guardar(usuario)
    sesion.iniciar(usuario)
    return usuario
