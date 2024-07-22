from django.db import models
import datetime

class Produto(models.Model):
    produto = models.CharField(max_length=200)
    preco = models.FloatField()

    def __str__(self):
        return self.produto

class Funcionario(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    produto_vendido = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome_vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"{self.produto_vendido}"



