# Generated by Django 4.2.7 on 2023-12-04 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0017_rename_episodio_video_episode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='collection',
        ),
    ]
