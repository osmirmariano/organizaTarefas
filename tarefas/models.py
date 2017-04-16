# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tarefas(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    descricao_detalhada = models.CharField(max_length=300)
    ano_inicio = models.DateField()
    ano_final = models.DateField()

    def __unicode__(self):
        return '{0} - {1} - {2} - {3} - {4}'.format(self.titulo, self.descricao, self.descricao_detalhada, self.ano_inicio, self.ano_final)