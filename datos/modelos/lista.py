from peewee import CharField, ForeignKeyField, IntegerField

from datos.model_base import ModelBase
from datos.modelos.tablero import Tablero


class Lista(ModelBase):
    titulo = CharField(max_length=200)
    posicion = IntegerField(default=1)
    tablero = ForeignKeyField(Tablero, backref="listas", on_delete="CASCADE")

    class Meta:
        table_name = "listas"

    def __str__(self) -> str:
        return self.titulo
