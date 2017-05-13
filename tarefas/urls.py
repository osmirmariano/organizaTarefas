
from django.conf.urls import url
from tarefas import views

urlpatterns = [
    url(r'^$', views.ListarTarefas.as_view(), name='listar-tarefas'),
    url(r'adicionar$', views.AdicionarTarefas.as_view(), name='adicionar-tarefas'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.DeletarTarefas.as_view(), name='deletar-tarefas'),
    url(r'^(?P<pk>[0-9]+)/$', views.EditarTarefas.as_view(), name='editar-tarefas'),
    url(r'^visualizar/(?P<pk>[0-9]+)/$', views.VisualizarTarefas.as_view(), name='visualizar-tarefas'),
    url(r'^compartilhar/(?P<pk>[0-9]+)/$', views.CompartilharTarefas.as_view(), name='compartilhar-tarefas'),
    url(r'^compartilhamento/(?P<pk>[0-9]+)/$', views.Compartilhamento.as_view(), name='compartilhamento'),
    url(r'^tarefasCompartilhdaUsuario/(?P<pk>[0-9]+)/$', views.CompartilharTarefasUsuario.as_view(), name='compartilhar-usuario')
]