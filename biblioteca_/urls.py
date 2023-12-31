from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:id>/', views.livro_detail , name='product-detail'),
    path('create-book/', views.add_book, name='add_book'),
    path('delete-livro/<int:id>/', views.delete_livro, name='delete_livro'),
    path('empresta-livro/<int:id>/', views.empresta_livro, name='empresta_livro'),
    path('livro-indisponivel/', views.livro_indisponivel, name='livro_indisponivel'),
    path('livro-disponivel/', views.livro_disponivel, name='livro_disponivel'),
    path('search-livro/', views.search_livro, name='search_livro'),
    path('adicionar_genero/', views.adicionar_genero, name='adicionar_genero'),
    path('meus-livros/', views.livros_alugados, name='meus-livros'),
    path('devolve_livro/<int:livro_id>/', views.devolve_livro, name='devolve_livro')

]