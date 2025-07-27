from django.contrib.auth.models import User
from django.db import models


class Grade(models.Model):
    """
    Класс для хранения оценок пользователей к цитатам.

    Attributes:
        LIKE (int): Значение лайка (+1).
        DISLIKE (int): Значение дизлайка (-1).
        GRADE_CHOICES (list[tuple[int, str]]): Возможные варианты оценок.
        user (ForeignKey): Пользователь, поставивший оценку.
        quote (ForeignKey): Цитата, к которой дана оценка.
        grade (SmallIntegerField): Само значение оценки (лайк или дизлайк).

    """

    LIKE = 1
    DISLIKE = -1
    GRADE_CHOICES = [(LIKE, "Лайк"), (DISLIKE, "Дизлайк")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey("Quote", on_delete=models.CASCADE, related_name="grades")
    grade = models.SmallIntegerField(choices=GRADE_CHOICES)

    class Meta:
        unique_together = ("user", "quote")
        verbose_name = "оценка"
        verbose_name_plural = "оценки"

    def __str__(self):
        return f"{self.user.username}: {self.grade}"
