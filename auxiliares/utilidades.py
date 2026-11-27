"""Funciones auxiliares de formato (sin dependencias de otras capas)."""
import os

from . import constantes as c


def limpiar_pantalla() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def recortar(texto, maximo: int = c.MAX_CELDA_TABLA) -> str:
    texto = "" if texto is None else str(texto).replace("\n", " ")
    return texto if len(texto) <= maximo else texto[: maximo - 3] + "..."


def formatear_fecha(fecha) -> str:
    return "" if fecha is None else fecha.strftime(c.FORMATO_FECHA)


def si_no(valor: bool) -> str:
    return "Sí" if valor else "No"


def formatear_tabla(encabezados, filas) -> str:
    """Devuelve una tabla de texto alineada."""
    filas = [[recortar(celda) for celda in fila] for fila in filas]
    anchos = [len(h) for h in encabezados]
    for fila in filas:
        for i, celda in enumerate(fila):
            anchos[i] = max(anchos[i], len(celda))

    def linea_datos(fila):
        return "| " + " | ".join(celda.ljust(ancho) for celda, ancho in zip(fila, anchos)) + " |"

    separador = "+" + "+".join("-" * (ancho + 2) for ancho in anchos) + "+"
    partes = [separador, linea_datos(encabezados), separador]
    partes += [linea_datos(fila) for fila in filas]
    partes.append(separador)
    return "\n".join(partes)
