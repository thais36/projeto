from django.shortcuts import render, redirect


def home(request):
    eventos = Evento.objects.all()
    return render(request, 'index.html', {'eventos': eventos})


def salvar(request):
    vnome = request.POST('nome')
    evento.objects.create(nome=vnome)
    eventos = Evento.objects.all()
    return render(request, 'index.html', {'eventos': eventos})

def editar(request, id):
    evento = vento.objects.get(id=id)
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