from django.contrib import admin
from .models import *

class TarefasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'descricao', 'descricao_detalhada', 'ano_inicio', 'ano_final']
admin.site.register(Tarefas, TarefasAdmin)
# Register your models here.