# Generated by Django 2.2.3 on 2020-04-12 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lan', models.FloatField()),
                ('lon', models.FloatField()),
            ],
        ),
    ]