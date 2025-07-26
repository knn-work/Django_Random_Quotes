from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from quotes.forms import LikeForm, DislikeForm
from quotes.models import Quote, Grade


class AddLike(FormView):
    form_class = LikeForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))

        quote_id = kwargs.get('pk')
        quote = get_object_or_404(Quote, id=quote_id)
        self.success_url = reverse_lazy('quote', args=(quote_id,))

        try:
            grade = Grade.objects.get(user=request.user, quote=quote)

            # Если оценка существует, проверяем текущую оценку
            if grade.grade != Grade.LIKE:
                grade.grade = Grade.LIKE
                grade.save()
            else:
                # Пользователь уже поставил лайк ранее, удаляем запись
                grade.delete()

        except Grade.DoesNotExist:
            # Создание новой записи
            new_grade = Grade(
                user=request.user,
                quote=quote,
                grade=Grade.LIKE
            )
            new_grade.save()

        return super().post(request, *args, **kwargs)


class AddDislike(FormView):
    form_class = DislikeForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))

        quote_id = kwargs.get('pk')
        quote = get_object_or_404(Quote, id=quote_id)
        self.success_url = reverse_lazy('quote', args=(quote_id,))

        try:
            grade = Grade.objects.get(user=request.user, quote=quote)

            # Проверяем текущую оценку
            if grade.grade != Grade.DISLIKE:
                grade.grade = Grade.DISLIKE
                grade.save()
            else:
                # Пользователь уже поставил дизлайк ранее, удаляем запись
                grade.delete()

        except Grade.DoesNotExist:
            # Создаем новую запись
            new_grade = Grade(
                user=request.user,
                quote=quote,
                grade=Grade.DISLIKE
            )
            new_grade.save()

        return super().post(request, *args, **kwargs)
