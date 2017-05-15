from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tarefas.models import *
from tarefas import views
from django.contrib.auth.models import User
# Create your models here.
class CompartilhamentoUsuario(models.Model):
    usuario = models.ForeignKey(User)
    tarefa = models.ForeignKey(Tarefas)
    
    class Meta:
        unique_together = ("usuario", "tarefa")