from peewee import CharField, DateField, ForeignKeyField, IntegerField, TextField

from auxiliares.constantes import PRIORIDAD_POR_DEFECTO
from datos.model_base import ModelBase
from datos.modelos.lista import Lista
from datos.modelos.usuario import Usuario


class Tarjeta(ModelBase):
    titulo = CharField(max_length=200)
    descripcion = TextField(null=True)
    prioridad = CharField(max_length=10, default=PRIORIDAD_POR_DEFECTO)
    fecha_limite = DateField(null=True)
    posicion = IntegerField(default=1)
    lista = ForeignKeyField(Lista, backref="tarjetas", on_delete="CASCADE")
    asignado_a = ForeignKeyField(
        Usuario, backref="tarjetas_asignadas", null=True, on_delete="SET NULL"
    )

    class Meta:
        table_name = "tarjetas"

    def __str__(self) -> str:
        return self.titulo
