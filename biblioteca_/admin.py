from django.contrib import admin
from .models import Generos, Livros

class BooksAdmin(admin.ModelAdmin):
    list_display = ['titulo','genero', 'autor', 'qtd_exemplares']
    list_filter = ['titulo','genero', 'autor']
    list_filter = ['titulo','genero', 'autor']



admin.site.register(Livros, BooksAdmin)
admin.site.register(Generos)



# Register your models here.
