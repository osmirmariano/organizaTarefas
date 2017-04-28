from __future__ import unicode_literals

from django.db import models
from PIL import Image
# Create your models here.

class Cadastro(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    image = models.ImageField(upload_to='usuario', blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2} - {3}'.format(
            self.username,
            self.email,
            self.password
        )
        