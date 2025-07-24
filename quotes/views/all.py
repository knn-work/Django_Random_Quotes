from django.shortcuts import render

from quotes.models import Source, Quote




def all_source(request):
    sources = Source.objects.all()

    quotes = Quote.objects.all()
    return render(
        request,
        "all_quotes.html",
        context={
            'quotes':quotes
        },
    )
