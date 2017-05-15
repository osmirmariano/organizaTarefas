from django.shortcuts import render
from tarefas.models import Tarefas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from tarefas.forms import *
from django.contrib.auth import authenticate,logout 
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render
from compartilhamento.models import CompartilhamentoUsuario

# Create your views here.
class CompartilharTarefas(LoginRequiredMixin, View):
    """
    Formulario para excluir as tarefas
    """
    login_url = '/'

    def get(self, request, pk):
        context = {
            'object_list': User.objects.all(),
            'pk': pk
        }
        return render(request, 'compartilhamento/compartilhar.html', context)
   

class ListarCompartilhamento(LoginRequiredMixin, ListView):
    """
    Formulario para listar compartilhamento
    """
    login_url = '/'
    model = CompartilhamentoUsuario
    template_name = 'index.html'
    def get_queryset(self):
        queryset = CompartilhamentoUsuario.objects.filter(usuario=self.request.user)
        return queryset

class CompartilharTarefasUsuario(LoginRequiredMixin, View):
    """
    Instancias de compartilhamentos de tarefas
    """
    login_url = '/'

    def get(self, request, pk):
        usuario = User.objects.get(pk=pk)
        tarefas = Tarefas.objects.get(pk=pk)
        context = {
            'Tarefas': tarefas, 
            'Usuario': usuario
        }
        return render(request, 'index.html', context)


class EditarTarefasCompartilhada(LoginRequiredMixin, UpdateView):
    """
    Formulario para editar as tarefas
    """
    login_url = '/'
    model = CompartilhamentoUsuario
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar-tarefas')

#class Compartilhamento(LoginRequiredMixin, View):
#    """
#    Formulario para excluir as tarefas
#    """
#    login_url = '/'
#    def get(self, request):
#        context = {
#            'object_list': User.object_list.all()
#        }
#        return render(request, 'index.html', context)

