
from django.conf.urls import include, url
from django.contrib import admin
from autenticacao import views

urlpatterns = [
    url(r'^$', include('autenticacao.urls', namespace="autenticacao-usuario")),    
    url(r'^tarefas/', include('tarefas.urls')),
    url(r'^admin/', admin.site.urls),
]
