"""Validaciones reutilizables. Lanzan ErrorNegocio si el dato no es válido."""
import re
from datetime import date, datetime

from . import constantes as c
from . import mensajes as m
from .excepciones import ErrorNegocio

_RE_USUARIO = re.compile(r"^[a-z0-9_.]{3,30}$")
_RE_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def texto_obligatorio(valor, campo: str, maximo: int = 200) -> str:
    valor = (valor or "").strip()
    if not valor:
        raise ErrorNegocio(m.CAMPO_OBLIGATORIO.format(campo=campo))
    if len(valor) > maximo:
        raise ErrorNegocio(m.CAMPO_MUY_LARGO.format(campo=campo, maximo=maximo))
    return valor


def texto_opcional(valor, campo: str, maximo: int = 1000):
    valor = (valor or "").strip()
    if not valor:
        return None
    if len(valor) > maximo:
        raise ErrorNegocio(m.CAMPO_MUY_LARGO.format(campo=campo, maximo=maximo))
    return valor


def nombre_usuario(valor) -> str:
    valor = (valor or "").strip().lower()
    if not _RE_USUARIO.match(valor):
        raise ErrorNegocio(m.NOMBRE_USUARIO_INVALIDO)
    return valor


def email(valor) -> str:
    valor = texto_obligatorio(valor, "email", 120).lower()
    if not _RE_EMAIL.match(valor):
        raise ErrorNegocio(m.EMAIL_INVALIDO)
    return valor


def password(valor) -> str:
    valor = valor or ""
    if len(valor) < c.PASSWORD_MIN_LARGO:
        raise ErrorNegocio(m.PASSWORD_CORTA.format(minimo=c.PASSWORD_MIN_LARGO))
    if len(valor.encode("utf-8")) > c.PASSWORD_MAX_BYTES:
        raise ErrorNegocio(m.PASSWORD_MUY_LARGA.format(maximo=c.PASSWORD_MAX_BYTES))
    if not (re.search(r"[A-Za-z]", valor) and re.search(r"\d", valor)):
        raise ErrorNegocio(m.PASSWORD_DEBIL)
    return valor


def rol(valor) -> str:
    valor = (valor or "").strip().lower()
    if valor not in c.ROLES:
        raise ErrorNegocio(m.ROL_INVALIDO.format(opciones=", ".join(c.ROLES)))
    return valor


def prioridad(valor) -> str:
    valor = (valor or "").strip().lower()
    if valor not in c.PRIORIDADES:
        raise ErrorNegocio(m.PRIORIDAD_INVALIDA.format(opciones=", ".join(c.PRIORIDADES)))
    return valor


def fecha_opcional(valor):
    """Acepta None, '', date o 'AAAA-MM-DD'. Devuelve date o None."""
    if valor is None or valor == "":
        return None
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    try:
        return datetime.strptime(str(valor).strip(), c.FORMATO_FECHA).date()
    except ValueError:
        raise ErrorNegocio(m.FECHA_INVALIDA)


def entero(valor, minimo=None) -> int:
    try:
        numero = int(str(valor).strip())
    except (TypeError, ValueError):
        raise ErrorNegocio(m.ENTERO_INVALIDO)
    if minimo is not None and numero < minimo:
        raise ErrorNegocio(m.NUMERO_MINIMO.format(minimo=minimo))
    return numero
