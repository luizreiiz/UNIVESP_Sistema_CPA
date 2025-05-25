from django.contrib import admin

# Register your models here.
from .models import Colaboradores, Genitores, Populacao, Pasto

class ColaboradoresAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'funcao' , 'telefone')
class GenitoresAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'sexo' , 'preco_animal')
class PopulacaoAdmin(admin.ModelAdmin):
    list_display = ('nome' , 'quantidade' , 'preco')
class PastoAdmin(admin.ModelAdmin):
    list_display = ('id_pasto', 'tamanho', 'piquetes', 'reforma')

admin.site.register(Colaboradores , ColaboradoresAdmin)
admin.site.register(Genitores, GenitoresAdmin )
admin.site.register(Populacao, PopulacaoAdmin)
admin.site.register(Pasto, PastoAdmin)