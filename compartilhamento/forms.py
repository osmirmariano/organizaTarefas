# -*- coding: utf-8 -*-
from django import forms
from compartilhamento.models import *

class CompartilhamentoForm(forms.ModelForm):
    class Meta:
        model = CompartilhamentoUsuario
        exclude = ['usuario']
        
        def __int__(self, *args, **kawargs):
		    super(CompartilhamentoForm, self).__init__(*args, **kwargs)