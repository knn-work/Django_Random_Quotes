from django.shortcuts import render

from quotes.models import Quote


def quote(request,pk:int, new_view:bool=True):
    quote_: Quote = Quote.objects.get(pk=pk)

    if new_view:
        quote_.increment_view_count()
    return render(
        request,
        "quote.html",
        context={
            'quote':quote_
        },
    )
