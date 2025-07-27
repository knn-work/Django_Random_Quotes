import random

from django.core.cache import cache
from django.db.models.aggregates import Sum
from django.shortcuts import redirect

from quotes.models import Quote


def random_quotes(request):
    quote:Quote = __get_random_quote()
    if quote is None:
        return redirect(f"/all")
    return redirect(f"/quote/{quote.pk}")

# Функция обновления суммарного веса
def update_total_weight():
    # Получаем актуальные данные из базы
    total_weight = Quote.objects.all().aggregate(total=Sum('weight'))['total'] or 0
    # Сохраняем результат в кэш
    cache.set('total_weight', total_weight)


# Функция получения рандомной цитаты
def __get_random_quote() -> Quote | None:
    # Сначала попытаемся достать общий вес из кэша
    total_weight = cache.get('total_weight')

    # Если данных в кэше нет - рассчитываем заново и сохраняем
    if not total_weight:
        update_total_weight()
        total_weight = cache.get('total_weight')

    # Генерация случайной точки
    random_point = random.uniform(0, total_weight)

    # Проходим по объектам и выбираем нужный объект
    current_point = 0
    for quote in Quote.objects.iterator():
        if current_point + quote.weight >= random_point:
            return quote
        current_point += quote.weight
    return None