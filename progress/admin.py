from django.contrib import admin
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

class WebsiteIdeaAdmin(admin.ModelAdmin):
  list_display = ('Website_Idea', 'Date')

class VisualStudioCodeLinkAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')

admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)
# Register your models here.
