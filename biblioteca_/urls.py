from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:id>/', views.livro_detail , name='product-detail'),
    path('create-book/', views.add_book, name='add_book'),
    path('delete-livro/<int:id>/', views.delete_livro, name='delete_livro'),
    path('empresta-livro/<int:id>/', views.empresta_livro, name='empresta_livro')

]