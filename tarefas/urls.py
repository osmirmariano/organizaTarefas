
from django.conf.urls import url
from tarefas import views

urlpatterns = [
    url(r'^$', views.ListarTarefas.as_view(), name='index'),
    url(r'adicionar$', views.AdicionarTarefas.as_view()),
    #url(r'^(?P<pk>[0-9]+)/$', views.editarTarefas.as_views(), name='editar-tarefas'),
    #url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletarTarefas.as_views(), name='deletar-tarefas'),
]