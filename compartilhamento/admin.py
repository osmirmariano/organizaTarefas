from django.contrib import admin
from .models import *

class CompartilhamentoAdmin(admin.ModelAdmin):
    list_display = ['tarefa', 'usuario']
admin.site.register(CompartilhamentoUsuario, CompartilhamentoAdmin)
# Register your models here.