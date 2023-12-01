from django.db import models
from django.contrib.auth.models import User

class Generos(models.Model):
    genero = models.CharField(max_length=255)
    
    def __str__(self):
        return self.genero
    
    class Meta:
        verbose_name=  'Genero'
        verbose_name_plural=  'Generos'

class Livros(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='livros_emprestados', verbose_name='Usuário')
    titulo = models.CharField(max_length=255)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    qtd_paginas = models.IntegerField()
    qtd_exemplares = models.IntegerField()
    capa = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    emprestado_para = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='livros_pegos_emprestado', verbose_name='Emprestado para')
    emprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class LivroAlugado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)


    
    def __str__(self):
        return f"{self.usuario.username} - {self.livro.titulo}"

    class Meta:
        verbose_name = 'Livro Alugado'
        verbose_name_plural = 'Livros Alugados'

# Create your models here.
