from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):  #Comando para fazer aparecer o nome no siteadmin
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100,blank=True) #Não são obrigatórios
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=150, blank=True) #Não são obrigatórios
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d') #fotos do ano, mês, dia
    def __str__(self):  #Comando para fazer aparecer o nome no siteadmin
        return self.nome