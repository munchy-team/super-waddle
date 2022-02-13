#from typing_extensions import Required
from django.db import models

# something is wrong here. 
class munchy(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateTimeField()
  Munchy_message = models.TextField(max_length=700, blank=True)

class Upload(models.Model):
    upload_file = models.FileField()    
    upload_date = models.DateTimeField(auto_now_add =True)

class DriveUploader(models.Model):    
    Title = models.CharField(max_length=100)
    drive_file_link = models.URLField(max_length=1000)
    Name_of_file = models.CharField(max_length=100)