from django.db.models import Case, When
from django.db.models.aggregates import Count
from django.shortcuts import render

from quotes.models import Quote, Grade


def top_quotes(request):
    # Собираем цитаты с наибольшим числом лайков
    top_quotes_ = Quote.objects.annotate(
        num_likes=Count(Case(When(grades__grade=Grade.LIKE, then=1)))
    ).order_by('-num_likes')[:10]

    context = {
        'top_quotes': top_quotes_
    }
    return render(request, 'top_quotes.html', context)
