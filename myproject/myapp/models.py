from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(max_length=100)
    preco = models.FloatField(max_length=100)

    def __str__(self):
        return self.nome


