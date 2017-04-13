from tarefas.models import Tarefas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from tarefas.forms import *

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
    success_url = reverse_lazy('index')


class EditarTarefas(UpdateView):
    """
    Formulario para editar as tarefas
    """
    model = Tarefas
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('index')

class DeletarTarefas(DeleteView):
    """
    Formulario para excluir as tarefas
    """
    model = Tarefas
    template_name = 'tarefas/deletar.html'
    success_url = reverse_lazy('index')
