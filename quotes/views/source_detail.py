from django.shortcuts import render, get_object_or_404

from quotes.models import Source, Quote


def source_detail(request, pk):
    # Извлекаем источник по PK
    source = get_object_or_404(Source, pk=pk)
    # Получаем все цитаты этого источника
    quotes = Quote.objects.filter(source=source)

    context = {
        'source': source,
        'quotes': quotes
    }
    return render(request, 'source_detail.html', context)
