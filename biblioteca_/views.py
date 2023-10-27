from django.shortcuts import render, HttpResponse
from .models import Livros

def index(request):
    livros = Livros.objects.all()

    return render(request, 'pages/index.html', {'livros':livros})

def livro_detail(request, id):
    livro = Livros.objects.get(id=id)

    return render(request, 'pages/livro_detail.html',{'livro':livro})
# Create your views here.
