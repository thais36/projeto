from django.shortcuts import render, redirect


def home(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'index.html', {'campeonatos': campeonatos})


def salvar(request):
    vnome = request.POST('nome')
    Campeonato.objects.create(nome=vnome)
    campeonatos = Campeonato.objects.all()
    return render(request, 'index.html', {'campeonatos': campeonatos})

def editar(request, id):
    campeonato = Campeonato.objects.get(id=id)
    return render(request, 'update.html', {'campeonatos': campeonatos})

def update(request, id):
    vnome = request.POST.get('nome')
    campeonato = Campeonato.objects.get(id=id)
    campeonato.nome = vnome
    campeonato.save()
    return redirect(home)   

def delete(request, id):
    campeonato = Campeonato.objects.get(id=id)
    campeonato.delete()
    return redirect(home) 