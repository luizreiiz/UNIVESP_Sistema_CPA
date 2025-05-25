from django.db import models

# Create your models here.

class Colaboradores(models.Model):
    nome = models.CharField("Nome", max_length = 100)
    telefone = models.CharField("Telefone", max_length = 100)
    cpf = models.CharField("CPF", max_length=100)
    funcao = models.CharField("Função", max_length=100)
    contratacao = models.DateField("Data de Contratação")

    def __str__(self):
        return self.nome

class Genitores(models.Model):
    nome = models.CharField("Identificação", max_length = 100)
    sexo = models.CharField("Sexo", max_length=100)
    data = models.DateField("Nascimento")
    gen_masc = models.CharField("Genitor Masculino (NA = desconhecido)", max_length=100)
    gen_fem = models.CharField("Genitor Feminino (NA = desconhecido)", max_length=100)
    preco_animal = models.DecimalField("Valor estimado do animal", decimal_places= 2, max_digits=8)
    preco_semen = models.DecimalField("Valor do Sêmen", decimal_places= 2, max_digits=8)

    def __str__(self):
        return self.nome


class Populacao(models.Model):
    nome = models.CharField("Nome", max_length = 100)
    quantidade = models.IntegerField("Número de animais")
    preco_animal = models.DecimalField("Valor estimado do animal", decimal_places=2, max_digits=8)
    preco = models.DecimalField("Preço da população", decimal_places=2, max_digits=8)
    sexo = models.TextField("Sexo")
    idade = models.DecimalField("Idade estimada", decimal_places= 2, max_digits=8)
    Genealogia = models.TextField("Genealogia (NA = desconhecido)")

    def __str__(self):
        return self.nome


class Pasto(models.Model):
    id_pasto = models.CharField("Nome", max_length = 100)
    tamanho = models.DecimalField("Tamanho (hectares)", decimal_places=2, max_digits=8)
    piquetes = models.IntegerField("Piquetes")
    reforma = models.DateField("Data de Reforma")
    tratamento = models.TextField("Adubos aplicados")
    custo = models.DecimalField("Custo estimado da última reforma", decimal_places=2, max_digits=8)

    def __str__(self):
        return self.id_pasto
