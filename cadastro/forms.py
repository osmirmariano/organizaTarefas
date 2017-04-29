# -*- coding: utf-8 -*-
from django import forms
from cadastro.models import *

class FormularioCadastro(forms.ModelForm):
    """
    Formulario para o model cadastro
    """
    class Meta:
        model = Cadastro
        exclude = []
    def __init__(self, *args, **kwargs):
        super(FormularioCadastro, self). __init__(*args, **kwargs)

        self.fields['username'].label = 'Nome do usuário'
        self.fields['email'].label = 'E-mail'
        self.fields['password'].label = 'Senha'
        self.fields['image'].label = 'Imagem de perfil'
