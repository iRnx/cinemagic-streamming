# Generated by Django 4.2.7 on 2023-11-25 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serie',
            name='imagem_detalhes',
            field=models.ImageField(default='', upload_to='images/detalhes'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='serie',
            name='imagem_thumb',
            field=models.ImageField(upload_to='images/thumb'),
        ),
    ]
