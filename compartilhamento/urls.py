
from django.conf.urls import url
from compartilhamento import views

urlpatterns = [
    url(r'^$', views.ListarCompartilhamento.as_view(), name='listar-compartilhamentos'),
    url(r'^(?P<pk>[0-9]+)/$', views.CompartilharTarefas.as_view(), name='compartilhar-tarefas'),
    url(r'^compartilhar/(?P<pk>[0-9]+)/$', views.CompartilharTarefasUsuario.as_view(), name='compartilhar-usuario'),
    url(r'^(?P<pk>[0-9]+)/$', views.EditarTarefasCompartilhada.as_view(), name='editar-tarefas-compartilhada')
    #url(r'^compartilhamento/(?P<pk>[0-9]+)/$', views.Compartilhamento.as_view(), name='compartilhamento'),
    
]