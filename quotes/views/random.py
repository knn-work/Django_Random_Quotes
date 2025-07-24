import random

from django.shortcuts import render

from quotes.models import Source, Quote


def random_quotes(request):
    quote:Quote = __get_random_quote()

    quote.increment_view_count()
    return render(
        request,
        "quote.html",
        context={
            'quote':quote
        },
    )

def __get_random_quote() -> Quote:
    quotes = list(Quote.objects.order_by("?").all())
    total_weight = sum(quote.weight for quote in quotes)

    random_point = random.uniform(0, total_weight)
    current_point = 0
    for quote in quotes:
        if current_point + quote.weight >= random_point:
            return quote
        current_point += quote.weight
    raise Exception("Пупупу")