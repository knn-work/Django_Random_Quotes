from django.contrib import admin

from quotes.models import Source, SourceType


@admin.register(SourceType)
class SourceTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ("label", "type")
    search_fields = ("label", "type__name")
    list_filter = ("type",)
    ordering = ("label",)
