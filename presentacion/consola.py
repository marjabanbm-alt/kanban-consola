"""Entrada y salida por consola: helpers reutilizables por todas las vistas."""
import maskpass

from auxiliares import constantes as c
from auxiliares import mensajes as m
from auxiliares import utilidades as u
from auxiliares import validaciones as v
from auxiliares.excepciones import ErrorNegocio


# ---------- Salida ----------
def titulo(texto: str) -> None:
    print("\n" + "=" * c.ANCHO_PANTALLA)
    print(f" {texto}")
    print("=" * c.ANCHO_PANTALLA)


def ok(texto: str) -> None:
    print(f"[OK] {texto}")


def error(texto: str) -> None:
    print(f"[ERROR] {texto}")


def info(texto: str) -> None:
    print(f"[i] {texto}")


def pausar() -> None:
    input(m.PRESIONE_ENTER)


def mostrar_tabla(encabezados, filas) -> None:
    print(u.formatear_tabla(encabezados, filas))


# ---------- Entrada ----------
def pedir_texto(prompt: str, defecto=None, obligatorio: bool = True) -> str:
    """Pide un texto. Con `defecto`, ENTER conserva el valor actual.
    En campos opcionales, '-' deja el valor vacío."""
    sufijo = f" [{defecto}]" if defecto not in (None, "") else ""
    ayuda = "" if obligatorio else " ('-' para vaciar)" if defecto else ""
    while True:
        valor = input(f"{prompt}{ayuda}{sufijo}: ").strip()
        if not valor and defecto is not None:
            return defecto
        if valor == "-" and not obligatorio:
            return ""
        if not valor and obligatorio:
            error(m.CAMPO_OBLIGATORIO.format(campo=prompt))
            continue
        return valor


def pedir_entero(prompt: str, defecto=None, minimo=None) -> int:
    sufijo = f" [{defecto}]" if defecto is not None else ""
    while True:
        texto = input(f"{prompt}{sufijo}: ").strip()
        if not texto and defecto is not None:
            return defecto
        try:
            return v.entero(texto, minimo)
        except ErrorNegocio as exc:
            error(str(exc))


def pedir_fecha(prompt: str, defecto=None):
    """Devuelve un date o None. ENTER conserva el valor; '-' lo vacía."""
    sufijo = f" [{u.formatear_fecha(defecto)}]" if defecto else ""
    while True:
        texto = input(f"{prompt} (AAAA-MM-DD, '-' para vaciar){sufijo}: ").strip()
        if not texto:
            return defecto
        if texto == "-":
            return None
        try:
            return v.fecha_opcional(texto)
        except ErrorNegocio as exc:
            error(str(exc))


def pedir_opcion(prompt: str, opciones, defecto: str) -> str:
    while True:
        texto = input(f"{prompt} ({'/'.join(opciones)}) [{defecto}]: ").strip().lower()
        if not texto:
            return defecto
        if texto in opciones:
            return texto
        error(f"Opciones válidas: {', '.join(opciones)}.")


def pedir_password(prompt: str = "Contraseña") -> str:
    """Lee una contraseña ocultando lo que se escribe (maskpass)."""
    return maskpass.askpass(prompt=f"{prompt}: ", mask="*")


def pedir_password_nueva(prompt: str = "Nueva contraseña"):
    """Pide la contraseña dos veces. Devuelve None si no coinciden."""
    primera = pedir_password(prompt)
    segunda = pedir_password("Repita la contraseña")
    if primera != segunda:
        error(m.PASSWORDS_NO_COINCIDEN)
        return None
    return primera


def confirmar(pregunta: str) -> bool:
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí"):
            return True
        if respuesta in ("n", "no"):
            return False


# ---------- Menús ----------
def ejecutar_seguro(accion) -> None:
    """Ejecuta una acción mostrando los errores de negocio sin cerrar la app."""
    try:
        accion()
    except ErrorNegocio as exc:
        error(str(exc))
    except (KeyboardInterrupt, EOFError):
        print()
        info(m.OPERACION_CANCELADA)
    except Exception as exc:  # último recurso para no perder la sesión del usuario
        error(f"{m.ERROR_INESPERADO}: {exc}")


def correr_menu(titulo_menu: str, opciones, texto_salida: str = "Volver") -> None:
    """Muestra un menú hasta que se elija 0. `opciones` = [(clave, texto, accion)]."""
    while True:
        titulo(titulo_menu)
        for clave, texto, _ in opciones:
            print(f"  {clave}. {texto}")
        print(f"  0. {texto_salida}")
        eleccion = input(m.SELECCIONE_OPCION).strip()
        if eleccion == "0":
            return
        accion = next((a for clave, _, a in opciones if clave == eleccion), None)
        if accion is None:
            error(m.OPCION_INVALIDA)
            continue
        ejecutar_seguro(accion)
        pausar()
