from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from quotes.forms import AddQuoteForm


@login_required
def add_quote(request):
    if request.method == 'POST':
        form = AddQuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.save()
            return redirect('/all')  # перенаправляем на страницу списка цитат
    else:
        form = AddQuoteForm()
    return render(request, 'add_quote.html', {'form': form})
