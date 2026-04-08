"""Formulários do aplicativo de reparos (rótulos e ajudas em português do Brasil)."""
from django import forms
from .models import Cliente, Equipamento, Tecnico, Reparo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo do cliente'
            }),
            'cep': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 00000-000',
                'id': 'id_cep'
            }),
            'endereco': forms.Textarea(attrs={
                'rows': 3, 
                'class': 'form-control',
                'placeholder': 'Digite o endereço completo'
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: (11) 99999-9999'
            }),
        }

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome completo do técnico'
            }),
        }

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
        widgets = {
            'id_cliente': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'marca': forms.Select(attrs={
                'class': 'form-select'
            }),
            'modelo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Galaxy S21, Inspiron 15, iPad Air'
            }),
            'numero_serial': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: BR-SN123456789'
            }),
        }

class ReparoForm(forms.ModelForm):
    class Meta:
        model = Reparo
        fields = '__all__'
        widgets = {
            'id_equipamento': forms.Select(attrs={
                'class': 'form-select'
            }),
            'id_tecnico': forms.Select(attrs={
                'class': 'form-select'
            }),
            'data_entrada': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'data_saida': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'descricao_defeito': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Descreva detalhadamente o defeito apresentado pelo equipamento'
            }),
            'descricao_reparo': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control',
                'placeholder': 'Descreva o reparo realizado e os procedimentos executados'
            }),
            'pecas_substituidas': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': 'Liste as peças substituídas (opcional)'
            }),
            'custo_reparo': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control',
                'placeholder': '0.00'
            }),
        } 