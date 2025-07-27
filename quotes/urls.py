from django.urls import include, path

from quotes.views import (
    AddDislike,
    AddLike,
    all_quotes,
    top_quotes,
    source_detail,
    random_quotes,
    quote,
    add_quote,
    AddSourceView,
)

urlpatterns = [
    path("", random_quotes, name="random"),
    path("top", top_quotes, name="top_quotes"),
    path("all", all_quotes, name="all_quotes"),
    path("quote/<int:pk>", quote, name="quote"),
    path("add_quote/", add_quote, name="add_quote"),
    path("quote/<int:pk>/like", AddLike.as_view(), name="add_like"),
    path("quote/<int:pk>/dislike", AddDislike.as_view(), name="add_dislike"),
    path("add_source/", AddSourceView.as_view(), name="add_source"),
    path("source/<int:pk>/", source_detail, name="source_detail"),
    path("", include("accounts.urls")),
]
