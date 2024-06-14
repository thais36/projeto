from django.shortcuts import render, redirect
from .models import Evento

def home(request):
    eventos = Evento.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})


def salvar(request):
    vnome = request.POST('nome')
    Evento.objects.create(nome=vnome)
    eventos = Evento.objects.all()
    return render(request, 'evento.html', {'eventos': eventos})

def editar(request, id):
    evento = evento.objects.get(id=id)
    return render(request, 'update.html', {'eventos': eventos})

def update(request, id):
    vnome = request.POST.get('nome')
    evento = Evento.objects.get(id=id)
    evento.nome = vnome
    evento.save()
    return redirect(home)   

def delete(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect(home) 