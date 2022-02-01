from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
  list_display = ('Link_Name', 'URL', 'Time')
admin.site.register(LinkAdmin)
# Register your models here.
