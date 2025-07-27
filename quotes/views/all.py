from django.shortcuts import render

from quotes.models import Quote


def all_quotes(request):
    headers = {
        "id": "pk",
        "Тип источника":"source__type",
        "Источник":"source__label",
        "Текст цитаты":"text",
        "Вес цитаты":"weight",
        "Просмотры":"view_count",
        "❤️":"",
        "💔":"",
    }
    sort_by = request.GET.get("sort_by")
    direction = request.GET.get("direction",'asc')

    quotes = Quote.objects.all()
    if sort_by:
        order_field =f"{"-" if direction == "desc" else ""}{sort_by}"
        quotes = quotes.order_by(order_field)

    return render(
        request,
        "all_quotes.html",
        context={
            'quotes':quotes,
            'headers':headers,
            'sort_by':sort_by,
            'direction':direction,
            # 'debug':request,
        },
    )
