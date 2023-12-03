from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Livros, Generos
from .models import Livros, LivroAlugado


from django.shortcuts import render, redirect, get_object_or_404
from .models import Livros, Generos
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

        if int(qtd_exemplares) > 0:
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
        # else:
        #     messages.error(request, 'A quantidade de exemplares deve ser maior que zero.')

    generos = Generos.objects.all()   
    return render(request, 'pages/add-book.html', {'generos': generos})

@login_required(redirect_field_name='login')   
def adicionar_genero(request):
    if request.method == 'POST':
        novo_genero = request.POST.get('novo_genero')

        if novo_genero:
            Generos.objects.create(genero=novo_genero)

        return redirect('adicionar_genero')  
    return redirect( 'home')

@login_required(redirect_field_name='login')
def index(request):
    livros = Livros.objects.all()

    return render(request, 'pages/index.html', {'livros':livros})

@login_required(redirect_field_name='login')   
def livro_detail(request, id):
    livro = Livros.objects.get(id=id)

    return render(request, 'pages/livro_detail.html',{'livro':livro})

def delete_livro(request, id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('home')


# def empresta_livro(request, id):
#     livro = Livros.objects.get(id=id)
#     livro.qtd_exemplares -= 1
#     livro.save()
#     if livro.qtd_exemplares<1:
#         livro.in_stock = False
#         return redirect('home')
#     else:
#         return render(request, 'pages/livro_detail.html', {'livro': livro})



def empresta_livro(request, id):
    livro = get_object_or_404(Livros, id=id)

    # Verifica se o livro tem mais de um exemplar disponível
    if livro.qtd_exemplares > 0:
        # Atualiza o livro com as informações do empréstimo
        livro.qtd_exemplares -= 1
        livro.emprestado = True
        livro.emprestado_para = request.user
        livro.save()

        # Adiciona o livro alugado ao modelo LivroAlugado
        LivroAlugado.objects.create(usuario=request.user, livro=livro)

        # messages.success(request, f"Você pegou emprestado '{livro.titulo}'.")
    # else:
    #     messages.error(request, "Este livro não está disponível para empréstimo.")

    return redirect('home')



def devolve_livro(request, livro_id):
    livro = get_object_or_404(Livros, id=livro_id)

    # Verifica se o livro está emprestado
    if livro.emprestado:
        # Remove todas as instâncias associadas ao livro em LivroAlugado
        LivroAlugado.objects.filter(livro=livro).delete()

        # Atualiza as informações do livro após a devolução
        livro.emprestado = False
        livro.emprestado_para = None
        livro.qtd_exemplares += 1  # Aumenta a quantidade de exemplares disponíveis
        livro.save()

        # messages.success(request, f"Você devolveu o livro '{livro.titulo}'.")

    return redirect('home')  # Redireciona para a página de meus livros ou ajuste conforme necessário

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

@login_required(redirect_field_name='login') 
def livros_alugados(request):
    livros_alugados = LivroAlugado.objects.filter(usuario=request.user)
    return render(request, 'pages/meus-livros.html', {'livros_alugados': livros_alugados})
