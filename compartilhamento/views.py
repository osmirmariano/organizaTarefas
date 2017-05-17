from django.shortcuts import render
from tarefas.models import Tarefas
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from tarefas.forms import *
from compartilhamento.forms import *
from compartilhamento.models import CompartilhamentoUsuario
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class CompartilharTarefas(LoginRequiredMixin, View):
    """
    Formulario para excluir as tarefas
    """
    login_url = '/'

    def get(self, request):
        id_tarefa = self.request.GET.get('id_tarefa','')
        context = {
            'object_list': User.objects.all(),
            'id_tarefa': id_tarefa
        }
        return render(request, 'compartilhamento/compartilhar.html', context)
   

class ListarCompartilhamento(LoginRequiredMixin, ListView):
    """
    Formulario para listar compartilhamento
    """
    login_url = '/'
    model = CompartilhamentoUsuario
    template_name = 'compartilhamento/listar.html'
    def get_queryset(self):
        queryset = CompartilhamentoUsuario.objects.filter(usuario=self.request.user)
        return queryset

class CompartilharTarefasUsuario(LoginRequiredMixin, View):
    """
    Instancias de compartilhamentos de tarefas
    """
    login_url = '/'
    print('teste')
    def get(self, request):
        compartilhamento = CompartilhamentoUsuario()
        id_tarefa = self.request.GET.get('id_tarefa','')
        id_usuario = self.request.GET.get('id_usuario','')
        tarefa = Tarefas.objects.get(id=id_tarefa)
        usuario = User.objects.get(id=id_usuario)
        compartilhamento.usuario = usuario
        compartilhamento.tarefa = tarefa
        compartilhamento.save()
        
        context = {
            'tarefas': tarefa, 
            'usuario': usuario
        }

        print(context)
        return render(request, 'compartilhamento/listar.html', context)


class EditarTarefasCompartilhada(LoginRequiredMixin, UpdateView):
    """
    Formulario para editar as tarefas
    """
    login_url = '/'
    model = CompartilhamentoUsuario
    form_class = FormularioTarefas
    template_name = 'tarefas/editar.html'
    success_url = reverse_lazy('listar-tarefas')





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

