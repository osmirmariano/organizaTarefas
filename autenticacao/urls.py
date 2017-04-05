from django.conf.urls import url
from autenticacao import views

urlpatterns = [
    url(r'^$', views.autenticacaoUsuario.as_view(), name='autenticacao-usuario'),
    url(r'^sair/', views.sair)
]

