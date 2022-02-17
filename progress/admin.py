#DO NOT SEND TO GITHUB INCOMPLTLE CODE WILL BREAK WEBSITE


from django.contrib import admin
<<<<<<< HEAD
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Assignment, Messages, File_Upload_Center, Statuses, ScheduledTasks
=======
from .models import Progresse, WebsiteIdea, VisualStudioCodeLink, Assignment, Messages, File_Upload_Center, Availability
>>>>>>> origin/Testing

class ProgresseAdmin(admin.ModelAdmin):
  list_display = ('name', 'date')

class WebsiteIdeaAdmin(admin.ModelAdmin):
  list_display = ('Website_Idea', 'Date')

class VisualStudioCodeLinkAdmin(admin.ModelAdmin):
  list_display = ('Title', 'Date')
  
class StatusesAdmin(admin.ModelAdmin):
  list_display = ('Document_Name',)

class AvailabilityAdmin(admin.ModelAdmin):
  list_display = ('Name', 'Available', 'On_Docs', 'Notes','Updated_At')



class AssignmentAdmin(admin.ModelAdmin):
  list_display = ('Name_Of_Assignment', 'Resolved','Date_Assigned','Assigned_By',  'Primary_Assigned_Person', 'Secondary_Assigned_Person', 'Tertiary_Assigned_Person','Due_Date', 'Latest_Important_Message','Message_Posted_At',)

class MessagesAdmin(admin.ModelAdmin):
  list_display = ('Message','From','To', 'date')

class File_Upload_CenterAdmin(admin.ModelAdmin):
  list_display = ('File_Name', 'Time')
  
class ScheduledTasksAdmin(admin.ModelAdmin):
  list_display = ('Task_Name', 'Due')

admin.site.register(Progresse, ProgresseAdmin)
admin.site.register(WebsiteIdea, WebsiteIdeaAdmin)
admin.site.register(VisualStudioCodeLink,VisualStudioCodeLinkAdmin)

admin.site.register(Assignment, AssignmentAdmin )
admin.site.register(Messages, MessagesAdmin )
<<<<<<< HEAD
admin.site.register(Statuses, StatusesAdmin )
admin.site.register(ScheduledTasks, ScheduledTasksAdmin )
=======
admin.site.register(Availability, AvailabilityAdmin)
>>>>>>> origin/Testing
#admin.site.register(File_Upload_Center,File_Upload_CenterAdmin )

# Register your models here.
