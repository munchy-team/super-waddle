from django.contrib import admin
from .models import Progresse

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

admin.site.register(Progresse, ProgresseAdmin)
# Register your models here.
