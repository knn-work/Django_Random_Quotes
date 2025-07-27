from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from quotes.forms import DislikeForm
from quotes.models import Grade, Quote


class AddDislike(FormView):
    form_class = DislikeForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse_lazy('login'))

        quote_id = kwargs.get('pk')
        quote = get_object_or_404(Quote, id=quote_id)

        try:
            grade = Grade.objects.get(user=request.user, quote=quote)

            # Проверяем текущую оценку
            if grade.grade != Grade.DISLIKE:
                grade.grade = Grade.DISLIKE
                grade.save()
            else:
                # Удаляем запись, если пользователь снова нажимает дизлайк
                grade.delete()

        except Grade.DoesNotExist:
            # Создаем новую запись
            new_grade = Grade(
                user=request.user,
                quote=quote,
                grade=Grade.DISLIKE
            )
            new_grade.save()

        # Возвращаем обновленные значения лайков и дизлайков
        return JsonResponse({'likes': quote.likes(), 'dislikes': quote.dislikes()})
