from peewee import CharField, ForeignKeyField, TextField

from datos.model_base import ModelBase
from datos.modelos.usuario import Usuario


class Tablero(ModelBase):
    titulo = CharField(max_length=200)
    descripcion = TextField(null=True)
    propietario = ForeignKeyField(Usuario, backref="tableros")

    class Meta:
        table_name = "tableros"

    def __str__(self) -> str:
        return self.titulo
