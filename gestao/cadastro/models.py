from django.db import models
#from .models import Pessoa
#from simplecep.fields import CepField
from django import forms

class Pessoa(models.Model):
    aluno = models.BooleanField(default=False)
    atleta = models.BooleanField(default=False)
    professor = models.BooleanField(default=False)
    outros = models.BooleanField(default=False)

    nome = models.CharField(max_length=256)
    cpf = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    telefone = models.CharField(max_length=256)
    curso = models.CharField(max_length=256)
    semestre = models.IntegerField()
  
    #cep = CepField()
    cep = models.CharField(max_length=256) 
    enderenco = models.CharField(max_length=256)
    numero_endereco = models.CharField(max_length=256)
    complemento = models.CharField(max_length=256)
    bairro = models.CharField(max_length=256)
    cidade = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'pessoa'
        verbose_name_plural = 'pessoas'
        verbose_name = 'pessoa'
        ordering = ['nome']
