from django.db import models

class Generos(models.Model):
    genero = models.CharField(max_length=255)
    
    def __str__(self):
        return self.genero
    
    class Meta:
        verbose_name=  'Genero'
        verbose_name_plural=  'Generos'

class Livros(models.Model):
    titulo = models.CharField(max_length=255)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    qtd_paginas = models.IntegerField()
    qtd_exemplares = models.IntegerField()
    capa = models.ImageField(blank=False)
    autor = models.CharField(max_length=255)
    # disponibilidade = models.BooleanField(default=True)
        
    def __str__(self):
        return self.titulo
    
    
    class Meta:
        verbose_name=  'Livro'
        verbose_name_plural=  'Livros'

# Create your models here.
