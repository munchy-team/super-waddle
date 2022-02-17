# hello it is fixed. 
# ow is 1 now easy pw py
#upload to github 
from django.contrib import admin

from testing.models import DriveUploader
from .models import munchy


class MunchyAdmin(admin.ModelAdmin):
  list_display = ('name','From','To', 'date','Munchy_Message')

class DriveAdmin(admin.ModelAdmin):
  list_display = ('Title', 'drive_file_link','Name_of_file','File_Type')

admin.site.register(munchy,MunchyAdmin)
admin.site.register(DriveUploader, DriveAdmin)

# Register your models here.
