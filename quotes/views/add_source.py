from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from quotes.models import Source


class AddSourceView(LoginRequiredMixin, CreateView):
    model = Source
    fields = ["type", "label"]
    template_name = "add_source.html"
    success_url = reverse_lazy("all_quotes")

    def form_valid(self, form):

        response = super().form_valid(form)
        return response