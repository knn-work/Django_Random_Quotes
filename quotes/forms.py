from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import CreateView

from quotes.models import Source, Quote


class AddQuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ["source", "text", "weight"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтруем доступные источники, оставляя только те, у которых менее трёх цитат
        self.fields["source"].queryset = Source.objects.annotate(
            quote_count=Count("quote")
        ).filter(quote_count__lt=3)

    def clean_text(self):
        data = self.cleaned_data["text"]
        if len(data.strip()) == 0:
            raise forms.ValidationError("Текст цитаты должен содержать символы")
        return data


class LikeForm(forms.Form):
    pass


class DislikeForm(forms.Form):
    pass
