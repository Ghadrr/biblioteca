from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Livros, Generos

from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros, Generos
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')

def add_book(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        genero_id = request.POST.get('genero')
        qtd_paginas = request.POST.get('qtd_paginas')
        qtd_exemplares = request.POST.get('qtd_exemplares')
        capa = request.FILES.get('capa')
        autor = request.POST.get('autor')

        # Obtenha a instância do modelo Generos com base no ID
        genero = get_object_or_404(Generos, id=genero_id)

        Livros.objects.create(
            user_id=request.user.id,
            titulo=titulo,
            genero=genero,
            qtd_paginas=qtd_paginas,
            qtd_exemplares=qtd_exemplares,
            capa=capa,
            autor=autor
        )

        return redirect('home')

    else:
        generos = Generos.objects.all()   
        return render(request, 'pages/add-book.html', {'generos': generos})
    
def adicionar_genero(request):
    if request.method == 'POST':
        novo_genero = request.POST.get('novo_genero')

        if novo_genero:
            Generos.objects.create(genero=novo_genero)

        # Após adicionar o gênero, redirecione para a página desejada
        return redirect('adicionar_genero')  # Substitua 'nome_da_pagina' pelo nome real da página

    return redirect( 'home')

def index(request):
    livros = Livros.objects.all()

    return render(request, 'pages/index.html', {'livros':livros})

def livro_detail(request, id):
    livro = Livros.objects.get(id=id)

    return render(request, 'pages/livro_detail.html',{'livro':livro})

def delete_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('home')


def empresta_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.qtd_exemplares -= 1
    livro.save()
    if livro.qtd_exemplares<1:
        livro.in_stock = False
        return redirect('home')
    else:
        return render(request, 'pages/livro_detail.html', {'livro': livro})

def livro_indisponivel(request):
    livros = Livros.objects.filter(qtd_exemplares=0)
    return render(request, 'pages/index.html', {'livros': livros})


def livro_disponivel(request):
    livros = Livros.objects.filter(qtd_exemplares__gte=1)
    return render(request, 'pages/index.html', {'livros': livros})

def search_livro(request):
    q = request.GET.get('q')
    livros = Livros.objects.filter(titulo__icontains=q)
    return render(request, 'pages/index.html', {'livros':livros})