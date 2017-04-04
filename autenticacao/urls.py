from django.conf.urls import url
from autenticacao import views

urlpatterns = [
    url(r'^$', views.autenticacaoUsuario.as_view(), name='autenticacao-usuario'),
    url(r'^$', views.logoutView.as_view(), name='logout-usuario'),
]

