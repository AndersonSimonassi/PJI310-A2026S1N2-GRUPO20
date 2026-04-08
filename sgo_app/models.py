"""Modelos de dados: clientes, técnicos, equipamentos e reparos."""
from django.db import models

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=200)
    cep = models.CharField('CEP', max_length=15, blank=True, null=True)
    endereco = models.TextField('Endereço')
    telefone = models.CharField('Telefone', max_length=20)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'reparo_cliente'

    def __str__(self):
        return self.nome

class Tecnico(models.Model):
    id_tecnico = models.AutoField(primary_key=True)
    nome = models.CharField('Nome do Técnico', max_length=200)

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        db_table = 'reparo_tecnico'

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    BRAND_CHOICES = [
        ('APPLE', 'Apple'),
        ('SAMSUNG', 'Samsung'),
        ('LG', 'LG'),
        ('SONY', 'Sony'),
        ('MOTOROLA', 'Motorola'),
        ('ASUS', 'Asus'),
        ('ACER', 'Acer'),
        ('DELL', 'Dell'),
        ('HP', 'HP'),
        ('LENOVO', 'Lenovo'),
        ('OUTRAS', 'Outras marcas'),
    ]

    TYPE_CHOICES = [
        ('CELULAR', 'Celular'),
        ('TABLET', 'Tablet'),
        ('NOTEBOOK', 'Notebook'),
        ('CAMERA', 'Câmera'),
        ('TV', 'Televisor'),
        ('SOM', 'Aparelho de Som'),
        ('MICROONDAS', 'Microondas'),
        ('OUTROS', 'Outros'),
    ]

    id_equipamento = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    tipo = models.CharField('Tipo', max_length=50, choices=TYPE_CHOICES)
    marca = models.CharField('Marca', max_length=50, choices=BRAND_CHOICES)
    modelo = models.CharField('Modelo', max_length=100)
    numero_serial = models.CharField('Número de série', max_length=100)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'
        db_table = 'reparo_equipamento'

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.numero_serial}"

class Reparo(models.Model):
    id_reparo = models.AutoField(primary_key=True)
    id_equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, verbose_name='Equipamento')
    id_tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE, verbose_name='Técnico')
    data_entrada = models.DateField('Data de Entrada')
    data_saida = models.DateField('Data de Saída', null=True, blank=True)
    descricao_defeito = models.TextField('Descrição do Defeito')
    descricao_reparo = models.TextField('Descrição do Reparo')
    pecas_substituidas = models.TextField('Peças Substituídas', blank=True)
    custo_reparo = models.DecimalField('Custo do Reparo', max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Reparo'
        verbose_name_plural = 'Reparos'
        db_table = 'reparo_reparo'

    def __str__(self):
        return f'Reparo nº {self.id_reparo} — {self.id_equipamento}' 