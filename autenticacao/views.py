
# -*- coding: utf-8 -*-
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout #import do django para permitir a autenticação (authenticate - para verifica se o usuário)

class autenticacaoUsuario(View):
    """
    Autenticação de usuários
    """

    def get(self, request):
        context = {}
        if self.request.user and self.request.user.is_active:
                return render(request, 'autenticacao/mostra.html', context)
        return render(request, 'autenticacao/login.html', context)

    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                if user.is_active:
                        login(self.request, user)
                        return render(request, 'autenticacao/mostra.html', context)
                else:
                        context.update(message='Usuário inativo')
        else:
                context.update(message='Usário e/ou senha incorreto')
        return render (request, 'autenticacao/login.html', context)

class logoutView(View):
    """
    Para logout do usuário
    """
    def logout_view(self, request):
        context = {}
        logout(self, request)
        return render (request, 'autenticacao/login.html', context)