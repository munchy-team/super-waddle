from django.contrib import admin
from .models import MunchyApp

class MunchyAppAdmin(admin.ModelAdmin):
    list_display = ('AppName', 'AppCreator','DateCreated')

admin.site.register(MunchyApp, MunchyAppAdmin)

# Register your models here.


