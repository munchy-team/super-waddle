from django.contrib import admin
from .models import MunchyApps

class MunchyAppsAdmin(admin.ModelAdmin):
    list_display = ('AppName', 'AppCreator','DateCreated')

admin.site.register(MunchyApps, MunchyAppsAdmin)

# Register your models here.

