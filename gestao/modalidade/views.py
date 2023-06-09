from django.shortcuts import render, redirect


def home(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'index.html', {'modalidades': modalidades})


def salvar(request):
    vnome = request.POST('nome')
    Modalidade.objects.create(nome=vnome)
    modalidades = Mdalidade.objects.all()
    return render(request, 'index.html', {'modalidades': modalidades})

def editar(request, id):
    modalidade = Modalidade.objects.get(id=id)
    return render(request, 'update.html', {'modalidades': modalidades})

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