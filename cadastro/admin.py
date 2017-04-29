from django.contrib import admin
from .models import *

class CadastroAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'image']
admin.site.register(Cadastro, CadastroAdmin)
#Register your models here.