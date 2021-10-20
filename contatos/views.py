from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value  #Or
from django.db.models.functions import Concat

def index(request):
    contatos = Contato.objects.order_by('-id')   #Ordenar
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)


    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')  #Concatendo ambos e simulando um campo.

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__contains=termo)  #Busca completa.
    )

    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })


