# Generated by Django 5.0.2 on 2024-03-21 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestoes', '0006_remove_curso_alunos_remove_curso_dias_aula_alunos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aula',
            name='nome',
        ),
    ]
