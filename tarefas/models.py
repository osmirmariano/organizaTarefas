# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tarefas(models.Model):

    dono = models.ForeignKey(User, related_name='tarefas')
    titulo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    descricao_detalhada = models.TextField()
    ano_inicio = models.DateField()
    ano_final = models.DateField()

    def __unicode__(self):
        return '{0} - {1} - {2} - {3} - {4}'.format(
            self.titulo,
            self.descricao,
            self.descricao_detalhada,
            self.ano_inicio,
            self.ano_final
        )


class Compartilhamento(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    tarefa = models.ForeignKey(Tarefas, on_delete = models.CASCADE)
    
    class Meta:
        unique_together = ("usuario", "tarefa")