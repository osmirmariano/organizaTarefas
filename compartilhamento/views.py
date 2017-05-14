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

# Create your views here.
class CompartilharTarefas(LoginRequiredMixin, View):
    """
    Formulario para excluir as tarefas
    """
    login_url = '/'

    def get(self, request, pk):
        context = {
            'object_list': User.objects.all()
        }
        return render(request, 'compartilhamento/compartilhar.html', context)
   


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