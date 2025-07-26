from django.urls import path, include

from quotes.views import all_quotes, AddLike, AddDislike
from quotes.views.quote import quote
from quotes.views.random import random_quotes

urlpatterns = [
    path("", random_quotes, name="random"),
    path("all", all_quotes, name="all_quotes"),

    path("quote/<int:pk>", quote, name="quote"),
    path("quote/<int:pk>/like", AddLike.as_view(), name="add_like"),
    path("quote/<int:pk>/dislike", AddDislike.as_view(), name="add_dislike"),

    path('', include('accounts.urls')),

]
