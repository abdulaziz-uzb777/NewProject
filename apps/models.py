
from django.db.models import Model
from django.db.models.fields import TextField
from django.forms import CharField, FloatField


class Planet(Model):
    title = CharField(max_length=20)
    diameter = FloatField()
    distance = FloatField()
    description = TextField()

    def __str__(self):
        return self.title


