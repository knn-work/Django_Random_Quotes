from django.urls import path

from quotes.views import index, all_quotes
from quotes.views.random import random_quotes

urlpatterns = [
    path("", random_quotes, name="random"),
    path("all", all_quotes, name="all_quotes"),
    path("main", index, name="index"),
]
