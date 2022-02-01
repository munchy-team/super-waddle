# hello it is fixed. 
# ow is 1 now easy pw py
#upload to github 
from django.contrib import admin
from .models import munchy


class MunchyAdmin(admin.ModelAdmin):
  list_display = ('name', 'date','Munchy_message')
admin.site.register(munchy,MunchyAdmin)


# Register your models here.
