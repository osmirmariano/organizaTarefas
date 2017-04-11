# -*- coding: utf-8 -*-
from django import forms
from tarefas.models import *

class FormularioTarefas(forms.ModelForm):
    """
    Formulario para o model Tarefas
    """
    class Meta:
        model = Tarefas
        exclude = []