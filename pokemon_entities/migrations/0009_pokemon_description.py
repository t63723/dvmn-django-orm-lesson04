# Generated by Django 2.2.3 on 2020-04-17 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0008_auto_20200417_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='', verbose_name='Описание'),
        ),
    ]
