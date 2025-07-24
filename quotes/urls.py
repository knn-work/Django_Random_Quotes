from django.urls import path

from quotes.views import index, all_source
from quotes.views.random import random_quotes

urlpatterns = [
    path("", random_quotes, name="random"),
    path("all", all_source, name="all"),
    path("main", index, name="index"),
]
