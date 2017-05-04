from tarefas.models import Tarefas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from tarefas.forms import *
from django.contrib.auth import authenticate,logout 
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from tarefas.models import Tarefas

class ListarTarefas(LoginRequiredMixin, ListView):
    """
    Formulario para listas as tarefas adicionadas
    """
    model = Tarefas
    template_name = 'index.html'
    login_url = '/'
    def get_queryset(self):
        queryset = Tarefas.objects.filter(dono=self.request.user)
        return queryset


class AdicionarTarefas(LoginRequiredMixin, CreateView):
    login_url = '/'
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/adicionar.html'
    success_url = reverse_lazy('listar-tarefas')

    def form_valid(self, form):
        form.instance.dono = self.request.user
        return super(AdicionarTarefas, self).form_valid(form)


class EditarTarefas(LoginRequiredMixin, UpdateView):
    """
    Formulario para editar as tarefas
    """
    login_url = '/'
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar-tarefas')


class VisualizarTarefas(LoginRequiredMixin, UpdateView):
    """
    Formulario para editar as tarefas
    """
    login_url = '/'
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/visualizar.html'
   # success_url = reverse_lazy('visualizar-tarefas')

class DeletarTarefas(LoginRequiredMixin, DeleteView):
    """
    Formulario para excluir as tarefas
    """
    login_url = '/'
    model = Tarefas
    template_name = 'tarefas/excluir.html'
    success_url = reverse_lazy('listar-tarefas')
