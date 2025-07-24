
from django.shortcuts import render

from quotes.models import Source, Quote


def random_quotes(request):
    quote = Quote.objects.order_by("?").first()
    quote.increment_view_count()
    return render(
        request,
        "quote.html",
        context={
            'quote':quote
        },
    )

