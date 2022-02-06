#DO NOT SEND TO GITHUB INCOMPLTLE CODE WILL BREAK WEBSITE


from django.contrib import admin
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Excel, Assignment, Messages, File_Upload_Center

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

class File_Upload_CenterAdmin(admin.ModelAdmin):
  list_display = ('File_Name', 'Time')

admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)
admin.site.register(Excel, ExcelAdmin)
admin.site.register(Assignment, AssignmentAdmin )
admin.site.register(Messages, MessagesAdmin )
#admin.site.register(File_Upload_Center,File_Upload_CenterAdmin )

# Register your models here.
