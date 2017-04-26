from tarefas.models import Tarefas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from tarefas.forms import *
from django.contrib.auth import authenticate,logout 
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect


class ListarTarefas(ListView):
    """
    Formulario para listas as tarefas adicionadas
    """
    model = Tarefas
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ListarTarefas, self).get_context_data(**kwargs)
        return context


class AdicionarTarefas(CreateView):
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/adicionar.html'
    success_url = reverse_lazy('listar-tarefas')
    # def form_valid(self, form):
    #     ctx = self.get_context_data()
    #     print(ctx)
    #     self.object = form.save()
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        # return HttpResponseRedirect(self.get_success_url())


class EditarTarefas(UpdateView):
    """
    Formulario para editar as tarefas
    """
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar-tarefas')


class VisualizarTarefas(UpdateView):
    """
    Formulario para editar as tarefas
    """
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/visualizar.html'
   # success_url = reverse_lazy('visualizar-tarefas')

class DeletarTarefas(DeleteView):
    """
    Formulario para excluir as tarefas
    """
    model = Tarefas
    template_name = 'tarefas/excluir.html'
    success_url = reverse_lazy('listar-tarefas')
