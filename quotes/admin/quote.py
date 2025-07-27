from django.contrib import admin
from django.db.models import Count

from quotes.models import Quote, Source


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "text_preview",
        "source",
        "weight",
        "view_count",
        "likes",
        "dislikes",
    )
    search_fields = ("text", "source__name")
    list_filter = ("source",)
    ordering = ("-weight",)
    readonly_fields = ("view_count",)
    fields = ("source", "text", "weight", "view_count")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "source":
            kwargs["queryset"] = Source.objects.annotate(
                quote_count=Count("quote")
            ).filter(quote_count__lt=3)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def text_preview(self, obj):
        return obj.text[:50]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("source")
