# Generated by Django 2.2.3 on 2020-04-17 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0010_auto_20200417_0341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='title_js',
            new_name='title_jp',
        ),
    ]
