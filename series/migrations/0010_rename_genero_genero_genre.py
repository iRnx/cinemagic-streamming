# Generated by Django 4.2.7 on 2023-11-30 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0009_rename_ativo_serie_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genero',
            old_name='genero',
            new_name='genre',
        ),
    ]
