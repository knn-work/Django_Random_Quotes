from django.contrib import admin

from quotes.models import *

admin.site.register(Grade)

admin.site.register(Quote)
admin.site.register(Source)
admin.site.register(SourceType)