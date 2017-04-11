from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tarefas(models.Model):
    titulo = models.CharField(max_length=1000)
    descricao = models.CharField(max_length=1000)
    descricao_detalhada = models.CharField(max_length=100)
    ano_inicio = models.IntegerField()
    ano_final = models.IntegerField()

    def __str__(self):
        return '{0} - {1} - {2} - {3} - {4}'.format(self.titulo, self.descricao, self.descricao_detalhada, self.ano_inicio, self.ano_final)

