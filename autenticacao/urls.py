
from django.conf.urls import url, include
from autenticacao import views

urlpatterns = [
    url(r'^$', views.autenticacaoUsuario.as_view(), name='autenticacao-usuario'),
    url(r'^tarefas/sair/', views.Sair.as_view(), name='sair-sistema'),
    url(r'^$', views.Index.as_view(), name='index')
]