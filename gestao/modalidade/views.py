from django.shortcuts import render, redirect
from .models import Modalidade

def home(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'modalidade.html', {'modalidades': modalidades})


def salvar(request):
    vnome = request.POST('nome')
    Modalidade.objects.create(nome=vnome)
    modalidades = Modalidade.objects.all()
    return render(request, 'modalidade.html', {'modalidades': modalidades})

def editar(request, id):
    modalidade = Modalidade.objects.get(id=id)
    return render(request, 'update.html', {'modalidades': modalidade})

def update(request, id):
    vnome = request.POST.get('nome')
    modalidade = Modalidade.objects.get(id=id)
    modalidade.nome = vnome
    modalidade.save()
    return redirect(home)   

def delete(request, id):
    modalidade = Modalidade.objects.get(id=id)
    modalidade.delete()
    return redirect(home) 