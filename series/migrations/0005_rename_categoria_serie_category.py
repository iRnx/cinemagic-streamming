# Generated by Django 4.2.7 on 2023-11-30 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0004_rename_imagem_thumb_serie_image_thumb_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='categoria',
            new_name='category',
        ),
    ]
