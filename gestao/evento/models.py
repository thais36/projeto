from django.db import models
#from .models import Evento
from django import forms

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=256)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'evento'
        verbose_name_plural = 'evento'
        verbose_name = 'evento'
        ordering = ['nome']