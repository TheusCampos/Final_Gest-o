# Generated by Django 5.0.2 on 2024-03-06 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestoes', '0002_remove_aluno_data_de_nascimento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='curso',
        ),
    ]
