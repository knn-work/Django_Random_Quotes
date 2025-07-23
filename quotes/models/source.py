from django.db import models


class Source(models.Model):
    """
    Представляет источник цитаты (например, фильм, книга и др.)

    Attributes:
        type (ForeignKey): Тип источника (связан с моделью SourceType).
        label (CharField): Название источника (например, название фильма или книги).

    """

    type = models.ForeignKey("SourceType", on_delete=models.PROTECT)
    label = models.CharField(max_length=255)

    class Meta:
        verbose_name = "источник"
        verbose_name_plural = "источники"

    def __str__(self):
        return self.label


class SourceType(models.Model):
    """
    Описывает различные типы источников цитат (например, кино, литература и т.д.)

    Attributes:
        name (CharField): Название типа источника (например, "Фильм", "Книга").

    """

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "тип источника"
        verbose_name_plural = "типы источников"

    def __str__(self):
        return self.name
