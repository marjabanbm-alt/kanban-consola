"""Modelo base: configuración compartida por todos los modelos ORM."""
from datetime import datetime

from peewee import DateTimeField, Model

from datos.conexion import db


class ModelBase(Model):
    creado_en = DateTimeField(default=datetime.now)
    actualizado_en = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.actualizado_en = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db
