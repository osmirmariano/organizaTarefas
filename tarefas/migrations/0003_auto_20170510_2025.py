# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 23:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tarefas', '0002_auto_20170503_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compartilhamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarefa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefas.Tarefas')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='compartilhamento',
            unique_together=set([('usuario', 'tarefa')]),
        ),
    ]
