from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Endereco (models.Model):
    rua = models.CharField('Rua', max_length=30, default=None)
    numero = models.CharField('Numero', max_length=30, default=None)
    bairro = models.CharField('Bairro', max_length=30, default=None)
    complemento = models.CharField('Complemento', max_length=30, default=None)
    cep = models.CharField('cep', max_length=30, default=None)
    cidade = models.CharField('Cidade', max_length=30, default=None)

    class Meta:
        ordering = ('cidade', )

    def __str__(self):
        return self.cidade


class Funcionario (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField ('Nome', max_length=60, default=None)
    salario = models.FloatField ()
    contato = models.CharField('Contato', max_length=50, default=None)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome', )

    def __str__(self):
        return self.nome

class Cliente (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField ('Nome', max_length=60, default=None)
    dados_financeiros = models.CharField ('Dados', max_length=50)
    contato = models.CharField('Contato', max_length=50, default=None)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    class Meta:
        ordering = ('nome', )

    def __str__(self):
        return self.nome


class Agendamento (models.Model):
    tipo_veiculo = models.CharField ('Tipo de veiculo', max_length=60, default=None)
    marca_veiculo = models.CharField ('Marca veiculo', max_length=60, default=None)
    modelo_veiculo = models.CharField ('Modelo veiculo', max_length=60, default=None)
    ano_veiculo = models.CharField ('Ano veiculo', max_length=4, default=None)
    descricao = models.TextField ('Descricao', max_length=60, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        ordering = ('cliente', )

    def __str__(self):
        return self.cliente

class Venda (models.Model):
    numero_cartao = models.CharField ('Numero cartao', max_length=10, default=None)
    data_vencimento = models.DateField ('Data vencimento', default=None)
    cvv = models.CharField ('cvv', max_length=60, default=None)
    bandeira = models.CharField ('Bandeira', max_length=60, default=None)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        ordering = ('cliente', )

    def __str__(self):
        return self.cliente

class Orcamento (models.Model):
    mao_de_obra = models.FloatField ()
    valor_pecas = models.FloatField()
    tempo = models.FloatField()

    class Meta:
        ordering = ('tempo', )

    def __str__(self):
        return self.tempo


class Peca (models.Model):
    descricao = models.TextField('Descricao', max_length=100)
    quantidade = models.IntegerField()
    preco = models.FloatField()

    class Meta:
        ordering = ('preco', )

    def __str__(self):
        return self.preco