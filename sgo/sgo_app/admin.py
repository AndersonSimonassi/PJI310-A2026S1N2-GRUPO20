"""Configuração do painel administrativo do Django para os modelos do app."""
from django.contrib import admin
from .models import Cliente, Equipamento, Tecnico, Reparo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nome', 'telefone')
    search_fields = ('nome', 'telefone')
    list_filter = ('nome',)

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('id_tecnico', 'nome')
    search_fields = ('nome',)

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('id_equipamento', 'id_cliente', 'tipo', 'marca', 'modelo', 'numero_serial')
    list_filter = ('tipo', 'marca', 'id_cliente')
    search_fields = ('modelo', 'numero_serial', 'id_cliente__nome')

@admin.register(Reparo)
class ReparoAdmin(admin.ModelAdmin):
    list_display = ('id_reparo', 'id_equipamento', 'id_tecnico', 'data_entrada', 'data_saida', 'custo_reparo')
    list_filter = ('data_entrada', 'id_tecnico', 'id_equipamento__tipo')
    search_fields = ('id_equipamento__modelo', 'id_tecnico__nome', 'descricao_defeito')
