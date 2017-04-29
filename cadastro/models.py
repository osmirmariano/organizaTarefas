# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.core import validators
from django.db import models
import re
from PIL import Image
# Create your models here.

class Cadastro(models.Model):
    #username = models.CharField(max_length=100)
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True, validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'), 'O nome de usuário só pode conter letras, digitos ou os '
            'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, help_text=("Use '[algo]$[salt]$[hexdigest]' or use the <a href=\"password/\">change password form</a>."))
    image = models.ImageField(upload_to='usuario', blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(
            self.username,
            self.email,
            self.password
        )
        