from django.db import models
#from .models import Campeonato
from django import forms

class Campeonato(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.CharField(max_length=256)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=256)
    valor = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'campeonato'
        verbose_name_plural = 'campeonatos'
        verbose_name = 'campeonato'
        ordering = ['nome']
