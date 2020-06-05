from django.db import models


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок"
    )
    title_en = models.CharField(
        max_length=200,
        verbose_name="Заголовок на английском",
        default=""
    )
    title_jp = models.CharField(
        max_length=200,
        default="",
        verbose_name="Заголовок на японском"
    )
    previous_evolution = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="pokemon_previous_evolution",
        blank=True,
        null=True,
        default=None,
        verbose_name="Предыдущая эволюция"
    )
    image = models.ImageField(
        verbose_name="Картинка",
        default=None
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
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
        default=None,
        verbose_name="Дата и время появления",
        blank=True,
        null=True
    )
    disappeared_at = models.DateTimeField(
        default=None,
        verbose_name="Дата и время исчезновения",
        blank=True,
        null=True
    )
    level = models.IntegerField(
        default=None,
        verbose_name="Уровень",
        blank=True,
        null=True
    )
    health = models.IntegerField(
        default=None,
        verbose_name="Здоровье",
        blank=True,
        null=True
    )
    strength = models.IntegerField(
        default=None,
        verbose_name="Сила",
        blank=True,
        null=True,
    )
    defence = models.IntegerField(
        default=None,
        verbose_name="Защита",
        blank=True,
        null=True,
    )
    stamina = models.IntegerField(
        default=None,
        verbose_name="Выносливость",
        blank=True,
        null=True,
    )
