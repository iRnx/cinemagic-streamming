# Generated by Django 4.2.7 on 2023-12-04 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0018_remove_serie_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
