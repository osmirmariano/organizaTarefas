from tarefas.models import Tarefas
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from tarefas.forms import *

# class listarTarefas(ListView):
#     """
#     Formulario para listas as tarefas adiconadas
#     """
#     model = Tarefas
#     template_name = 'tarefas/listar.html'


class AdicionarTarefas(CreateView):
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/adicionar.html'
    success_url = reverse_lazy('adicionar-tarefas')


class EditarTarefas(UpdateView):
    """
    Formulario para editar as tarefas
    """
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar-tarefas')

class DeletarTarefas(DeleteView):
    """
    Formulario para excluir as tarefas
    """
    model = Tarefas
    template_name = 'tarefas/deletar.html'
    success_url = reverse_lazy('deletar-tarefas')