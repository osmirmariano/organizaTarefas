# Create your views here.
# -*- coding: utf-8 -*-
#from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from cadastro.models import Cadastro
from cadastro.forms import *

class Registrar(LoginRequiredMixin, CreateView):

    login_url = '/'

    model = Cadastro
    form_class = FormularioCadastro
    template_name = 'cadastro/registrar.html'
    success_url = reverse_lazy('autenticacao-usuario')