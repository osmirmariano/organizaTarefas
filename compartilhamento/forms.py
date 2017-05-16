# -*- coding: utf-8 -*-
from django import forms
from compartilhamento.models import *

class CompartilhamentoForm(forms.ModelForm):
    class Meta:
        model = CompartilhamentoUsuario
        exclude = ['usuario']