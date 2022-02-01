from django.contrib import admin
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Excel, Assignment, Messages, munchy

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

class WebsiteIdeaAdmin(admin.ModelAdmin):
  list_display = ('Website_Idea', 'Date')

class VisualStudioCodeLinkAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')

class ExcelAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')

class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('Task', 'Resolved','Date_Assigned', 'Assigned_To','Assigned_By', 'Due_Date', 'Latest_Important_Message','Message_Posted_At',)

class MessagesAdmin(admin.ModelAdmin):
  list_display = ('Message', 'Time','To', 'From','Response', 'Response_From','Time_Of_Response')
class MunchyAdmin(admin.ModelAdmin):
  list_display = ('name', 'date','Munchy_message')
admin.site.register(munchy,MunchyAdmin)
admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)
admin.site.register(Excel, ExcelAdmin)
admin.site.register(Assignment, AssignmentAdmin )
admin.site.register(Messages, MessagesAdmin )
# Register your models here.
