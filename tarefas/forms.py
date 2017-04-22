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
        
        self.fields['titulo'].label = 'Título:'
        self.fields['titulo'].widget.attrs['class'] = 'validate'
        self.fields['titulo'].widget.attrs['placeholder'] = 'Título da sua tarefas...'
        self.fields['titulo'].widget.attrs['required'] = 'required'
        
        self.fields['descricao'].label = 'Descrição:'
        self.fields['descricao'].widget.attrs['class'] = 'validate'
        self.fields['descricao'].widget.attrs['placeholder'] = 'Descrição da sua tarefa...'
        self.fields['descricao'].widget.attrs['required'] = 'required'

        self.fields['descricao_detalhada'].label = 'Descrição detalhada:'
        self.fields['descricao_detalhada'].widget.attrs['class'] = 'validate'
        self.fields['descricao_detalhada'].widget.attrs['placeholder'] = 'Descrição da sua tarefa...'
        self.fields['descricao_detalhada'].widget.attrs['required'] = 'required'

        self.fields['ano_inicio'].label = 'Data Início:'
        self.fields['ano_inicio'].widget.attrs['class'] = 'validate'
        self.fields['ano_inicio'].widget.attrs['placeholder'] = '00/00/0000'
        self.fields['ano_inicio'].widget.attrs['required'] = 'required'

        self.fields['ano_final'].label = 'Data Final:'
        self.fields['ano_final'].widget.attrs['class'] = 'validate'
        self.fields['ano_final'].widget.attrs['placeholder'] = '00/00/0000'
        self.fields['ano_final'].widget.attrs['required'] = 'required'
        
        