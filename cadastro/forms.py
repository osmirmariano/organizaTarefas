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