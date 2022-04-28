from django.contrib import admin
from .models import HomeBlog

class HomeBlogAdmin(admin.ModelAdmin):
    list_display = ('Post_Title','Date','Post_Author_MunchySite_Admin_Purposes_Only')

admin.site.register(HomeBlog, HomeBlogAdmin)