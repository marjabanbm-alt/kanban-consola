"""Configuración y manejo de la conexión a la base de datos (SQLite + Peewee)."""
from peewee import SqliteDatabase

from auxiliares.configuracion import RUTA_BD

# foreign_keys=1 activa la integridad referencial en SQLite
db = SqliteDatabase(RUTA_BD, pragmas={"foreign_keys": 1})


def conectar() -> None:
    if db.is_closed():
        db.connect()


def cerrar() -> None:
    if not db.is_closed():
        db.close()


def crear_tablas() -> None:
    """Crea las tablas de todos los modelos si no existen."""
    from datos.modelos import MODELOS  # import local para evitar ciclos

    conectar()
    db.create_tables(MODELOS, safe=True)
