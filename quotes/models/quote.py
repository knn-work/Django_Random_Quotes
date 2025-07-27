from django.core.exceptions import ValidationError
from django.db import models

from quotes.models import Grade


class Quote(models.Model):
    """
    Модель представления цитат.

    Attributes:
        source (ForeignKey): Источник цитаты (связан с моделью Source).
        text (TextField): Текст цитаты, уникален среди всех цитат.
        weight (PositiveIntegerField): Целочисленный показатель веса цитаты, влияет на вероятность отображения.
        view_count (PositiveIntegerField): Количество просмотров цитаты.
    """

    source = models.ForeignKey("Source", on_delete=models.CASCADE)
    text = models.TextField(unique=True)
    weight = models.PositiveIntegerField(default=1)
    view_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        count = Quote.objects.filter(source=self.source).count()
        if count > 3:
            raise ValidationError(
                f"Уже существует максимум допустимых цитат ({count }) из этого источника."
            )

        super().save(*args, **kwargs)

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=["view_count"])

    def likes(self) -> int:
        """Возвращает количество лайков"""
        return self.grades.filter(grade=Grade.LIKE).count()

    def dislikes(self):
        """Возвращает количество дизлайков"""
        return self.grades.filter(grade=Grade.DISLIKE).count()

    def voted_by_user(self, user):
        """Определяем, какая оценка была поставлена пользователем"""
        try:
            grade = self.grades.get(user=user)
            return grade.grade
        except Grade.DoesNotExist:
            return None

    class Meta:
        verbose_name = "цитата"
        verbose_name_plural = "цитаты"

    def __str__(self):
        return f"{self.text[:50]}..."
