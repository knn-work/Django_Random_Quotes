from django.urls import path

from quotes.views import index

urlpatterns = [
    path("", index, name="index"),
]
