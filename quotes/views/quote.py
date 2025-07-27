from django.shortcuts import render

from quotes.models import Quote

from django.http import JsonResponse


def quote(request, pk):
    quote_ = Quote.objects.get(pk=pk)

    quote_.increment_view_count()
    session_key = f"viewed_quote_{pk}"
    if not request.session.get(session_key):
        request.session[session_key] = True

    current_user_vote = None
    if request.user.is_authenticated:
        current_user_vote = quote_.voted_by_user(request.user)

    return render(
        request,
        "quote.html",
        context={'quote': quote_,
                 'current_user_vote': current_user_vote},

    )
