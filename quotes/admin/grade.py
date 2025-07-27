from django.contrib import admin

from quotes.models import Grade


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("user", "quote", "grade")

    list_filter = ("grade",)
    ordering = ("-pk",)
    raw_id_fields = ("user", "quote")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
