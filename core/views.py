from django.shortcuts import render

# Create your views here.
## Essas funções tem que ser importadas no URLs.py

from .models import Colaboradores
from .models import Genitores
from .models import Populacao
from .models import Pasto

import plotly.graph_objs as go
import plotly.offline as opy
from django.shortcuts import render




def index (request):
    return render(request, 'index.html' )

def colaboradores(request):
    colaboradores = Colaboradores.objects.all()
    context = {
        'colaboradores': colaboradores
    }
    return render(request , 'colaboradores.html', context)

def genitores(request):
    genitores = Genitores.objects.all()

    nomes = [g.nome for g in genitores]
    preco_animal = [float(g.preco_animal) for g in genitores]
    preco_semen = [float(g.preco_semen) for g in genitores]
    sexos = [g.sexo.upper() for g in genitores]

    # Contagem por sexo
    sexo_labels = ['M', 'F']
    sexo_values = [sexos.count('M'), sexos.count('F')]

    # Gráfico 1: Preço do Animal
    fig1 = go.Figure(data=[go.Bar(x=nomes, y=preco_animal, marker_color='green')])
    fig1.update_layout(title='Preço do Animal por Genitor', xaxis_title='Genitor', yaxis_title='Preço (R$)')
    grafico_animal = opy.plot(fig1, auto_open=False, output_type='div')

    # Gráfico 2: Preço do Sêmen
    fig2 = go.Figure(data=[go.Bar(x=nomes, y=preco_semen, marker_color='blue')])
    fig2.update_layout(title='Preço do Sêmen por Genitor', xaxis_title='Genitor', yaxis_title='Preço (R$)')
    grafico_semen = opy.plot(fig2, auto_open=False, output_type='div')

    # Gráfico 3: Distribuição por Sexo
    fig3 = go.Figure(data=[go.Bar(x=sexo_labels, y=sexo_values, marker_color=['red', 'purple'])])
    fig3.update_layout(title='Distribuição de Genitores por Sexo', xaxis_title='Sexo', yaxis_title='Quantidade')
    grafico_sexo = opy.plot(fig3, auto_open=False, output_type='div')

    context = {
        'genitores': genitores,
        'grafico_animal': grafico_animal,
        'grafico_semen': grafico_semen,
        'grafico_sexo': grafico_sexo,
    }
    return render(request, 'genitores.html', context)

def populacao(request):
    populacao = Populacao.objects.all()

    nomes = [p.nome for p in populacao]
    preco_animal = [float(p.preco_animal) for p in populacao]
    preco_total = [float(p.preco) for p in populacao]
    quantidades = [p.quantidade for p in populacao]

    # Gráfico 1: Preço por Animal
    fig1 = go.Figure([go.Bar(x=nomes, y=preco_animal, marker_color='teal')])
    fig1.update_layout(title='Preço por Animal (R$)', xaxis_title='Nome', yaxis_title='Preço por Animal')
    grafico_preco_animal = opy.plot(fig1, auto_open=False, output_type='div')

    # Gráfico 2: Preço Total da População
    fig2 = go.Figure([go.Bar(x=nomes, y=preco_total, marker_color='orange')])
    fig2.update_layout(title='Preço Total da População (R$)', xaxis_title='Nome', yaxis_title='Preço Total')
    grafico_preco_total = opy.plot(fig2, auto_open=False, output_type='div')

    # Gráfico 3: Quantidade de Animais
    fig3 = go.Figure([go.Bar(x=nomes, y=quantidades, marker_color='purple')])
    fig3.update_layout(title='Quantidade de Animais', xaxis_title='Nome', yaxis_title='Quantidade')
    grafico_quantidade = opy.plot(fig3, auto_open=False, output_type='div')

    context = {
        'populacao': populacao,
        'grafico_preco_animal': grafico_preco_animal,
        'grafico_preco_total': grafico_preco_total,
        'grafico_quantidade': grafico_quantidade
    }
    return render(request, 'populacao.html', context)

def pasto(request):
    pastos = Pasto.objects.all()

    nomes = [p.id_pasto for p in pastos]
    tamanhos = [float(p.tamanho) for p in pastos]
    piquetes = [p.piquetes for p in pastos]
    custos = [float(p.custo) for p in pastos]

    # Gráfico 1: Tamanho dos pastos
    fig1 = go.Figure([go.Bar(x=nomes, y=tamanhos, marker_color='green')])
    fig1.update_layout(title='Tamanho dos Pastos (hectares)', xaxis_title='Pasto', yaxis_title='Hectares')
    grafico_tamanho = opy.plot(fig1, auto_open=False, output_type='div')

    # Gráfico 2: Número de Piquetes
    fig2 = go.Figure([go.Bar(x=nomes, y=piquetes, marker_color='blue')])
    fig2.update_layout(title='Quantidade de Piquetes', xaxis_title='Pasto', yaxis_title='Piquetes')
    grafico_piquetes = opy.plot(fig2, auto_open=False, output_type='div')

    # Gráfico 3: Custo de Reforma
    fig3 = go.Figure([go.Bar(x=nomes, y=custos, marker_color='orange')])
    fig3.update_layout(title='Custo da Última Reforma (R$)', xaxis_title='Pasto', yaxis_title='Custo (R$)')
    grafico_custo = opy.plot(fig3, auto_open=False, output_type='div')

    context = {
        'pasto': pastos,
        'grafico_tamanho': grafico_tamanho,
        'grafico_piquetes': grafico_piquetes,
        'grafico_custo': grafico_custo
    }

    return render(request, 'pasto.html', context)

