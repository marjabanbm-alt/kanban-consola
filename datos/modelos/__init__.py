from datos.modelos.lista import Lista
from datos.modelos.tablero import Tablero
from datos.modelos.tarjeta import Tarjeta
from datos.modelos.usuario import Usuario

# Orden de creación respetando las claves foráneas
MODELOS = [Usuario, Tablero, Lista, Tarjeta]

__all__ = ["Usuario", "Tablero", "Lista", "Tarjeta", "MODELOS"]
