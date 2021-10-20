from django.contrib import admin
from .models import Contato, Categoria

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria', 'mostrar') #Categorias que irao aparecer
    list_display_links = ('nome', 'sobrenome') #Click
    list_filter = ('nome', 'sobrenome') #Filter
    search_fields = ('nome','sobrenome', 'telefone') #Campo de Busca
    list_editable = ('telefone', 'mostrar')


admin.site.register(Contato, ContatoAdmin)
admin.site.register(Categoria)
