from django.db import models


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name="Заголовок на английском",
        blank=True
    )
    title_jp = models.CharField(
        max_length=200,
        verbose_name="Заголовок на японском",
        blank=True
    )
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="pokemon_previous_evolution",
        verbose_name="Предыдущая эволюция",
        blank=True,
        null=True
    )
    image = models.ImageField(
        verbose_name="Картинка",
        blank=True
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name="entities",
        verbose_name="Покемон"
    )
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(
        verbose_name="Дата и время появления",
        blank=True,
        null=True
    )
    disappeared_at = models.DateTimeField(
        verbose_name="Дата и время исчезновения",
        blank=True,
        null=True
    )
    level = models.IntegerField(
        verbose_name="Уровень",
        blank=True,
        null=True
    )
    health = models.IntegerField(
        verbose_name="Здоровье",
        blank=True,
        null=True
    )
    strength = models.IntegerField(
        verbose_name="Сила",
        blank=True,
        null=True
    )
    defence = models.IntegerField(
        verbose_name="Защита",
        blank=True,
        null=True
    )
    stamina = models.IntegerField(
        verbose_name="Выносливость",
        blank=True,
        null=True
    )
