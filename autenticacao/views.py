
# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class autenticacaoUsuario(View):
    """
    Autenticação de usuários
    """
    def get(self, request):
        if self.request.user.is_authenticated():# and self.request.user.is_active:
                #return render(request, 'index.html', context)
                return redirect(reverse_lazy('index'))
        else:
                return render(request, 'autenticacao/login.html', {})

    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(self.request, user)
                        return redirect(reverse_lazy('listar-tarefas'))
                        #return redirect(request, 'index.html', context)
                        #return render(request, 'index.html', context)
                        #return redirect ('/')
                else:
                        context.update(message='Usuário inativo')
        else:
                context.update(message='Usuário e/ou senha incorreto')
        return render (request, 'autenticacao/login.html', context)

#class logout_View(View):

class Sair(LoginRequiredMixin,View):
        def get(self,request):
                logout(request)
                return redirect ('/')


class Index(View):
        def get(self, request):
                return render (request, 'index.html')