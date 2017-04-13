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
    def __init__(self, *args, **kwargs):
        super(FormularioTarefas, self). __init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['class'] = 'form-control'
        self.fields['titulo'].widget.attrs['placeholder'] = 'Titulo...'

        self.fields['descricao'].widget.attrs['class'] = 'form-control'
        self.fields['descricao_detalhada'].widget.attrs['class'] = 'form-control'
        self.fields['ano_inicio'].widget.attrs['class'] = 'form-control'
        self.fields['ano_final'].widget.attrs['class'] = 'form-control'
