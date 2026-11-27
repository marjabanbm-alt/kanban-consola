"""Configuraciones de la aplicación (rutas y nombre)."""
import os
from pathlib import Path

NOMBRE_APP = "Kanban Consola (estilo Trello)"
VERSION = "1.0.0"

BASE_DIR = Path(__file__).resolve().parent.parent

# La ruta de la base de datos puede sobreescribirse con la variable KANBAN_DB
RUTA_BD = os.getenv("KANBAN_DB", str(BASE_DIR / "kanban.db"))
RUTA_SQL = BASE_DIR / "datos" / "sql"
