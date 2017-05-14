
from django.conf.urls import include, url
from django.contrib import admin
from tarefas import views
from compartilhamento import views
from autenticacao import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('autenticacao.urls', namespace="autenticacao-usuario")),
    url(r'^tarefas/', include('tarefas.urls')),
    url(r'^compartilhamento/', include('compartilhamento.urls')),
    url(r'^cadastro/', include('cadastro.urls')),
    url(r'^index', views.Index.as_view(), name="index")
]
