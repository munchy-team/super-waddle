#hey is this working
#project doc thanks
# all is well deploy?


#from typing_extensions import Required
#<<<<<<< HEAD

#=======
#from unittest.util import _MAX_LENGTH
#>>>>>>> origin/Testing
from django.db import models

# something is wrong here. 
class munchy(models.Model):
  ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
  From = models.CharField(max_length=5, choices=ppl)
  To = models.CharField(max_length=5, choices=ppl)
  name = models.CharField(max_length=200)
  date = models.DateTimeField()
  Munchy_Message = models.TextField(max_length=700, blank=True)

class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)

class DriveUploader(models.Model):    
    Title = models.CharField(max_length=100)
    drive_file_link = models.URLField(max_length=1000, blank=True, help_text='If file is on Dropbox, go to Dropbox Link and select dropbox.com. Otherwise, leave "Dropbox Link" blank.')
    Name_of_file = models.CharField(max_length=100, blank=True)
    filetype = (
    ('-----', '-----'),
    ('Drive', 'Drive'),
    ('munchy', 'munchy'),  
     ('.docx', '.docx'),
     ('.xlsx', '.xlsx'), 
      ('.pptx', '.pptx'),
      ('.pdf', '.pdf'),
      ('Other', 'Other'),
      )
    File_Type = models.CharField(max_length=10, default="-----", choices=filetype)
    File_Link = models.URLField(max_length=2500, blank=True)
    fileln = (
    #('-----', '-----'),
    ('OneDrive', 'OneDrive'),
    ('Dropbox', 'Dropbox'),  
    ('Google Drive', 'Google Drive'),
    )
    File_Location = models.CharField(max_length=20, blank=True, choices=fileln)
    dbopt = (
    ('dropbox.com', 'dropbox.com'),
    )
    Dropbox_Link = models.CharField(max_length=25, blank=True, choices=dbopt, help_text="If file is on Dropbox, select dropbox.com, otherwise leave blank.")
    
  
# please make the migrations and migrate I will work on dwa. getting off docs too.

# okay have to work on dwa. I will be offline unfortunately. 