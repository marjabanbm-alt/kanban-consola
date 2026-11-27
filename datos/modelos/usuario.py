from peewee import BooleanField, CharField

from auxiliares.constantes import ROL_USUARIO
from datos.model_base import ModelBase


class Usuario(ModelBase):
    nombre_usuario = CharField(max_length=30, unique=True)
    nombre_completo = CharField(max_length=100)
    email = CharField(max_length=120, unique=True)
    password_hash = CharField(max_length=255)  # hash BCrypt, nunca texto plano
    rol = CharField(max_length=20, default=ROL_USUARIO)
    activo = BooleanField(default=True)

    class Meta:
        table_name = "usuarios"

    def __str__(self) -> str:
        return self.nombre_usuario
