from django.db import models
from django.shortcuts import render
from uuid import uuid4


class Modalidade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao_modalidade = models.CharField(max_length=255)
    local = models.CharField(max_length=256)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'modalidade'
        verbose_name_plural = 'modalidades'
        verbose_name = 'modalidade'
        ordering = ['nome']

    @staticmethod
    def listar_modalidades(request):
        modalidades = Modalidade.objects.all()
        return render(request, 'modalidades.html', {'modalidades': modalidades})
