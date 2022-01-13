from django.db import models

# Create your models here.

class Progress(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  notes = models.CharField(max_length=5000)
  #######Upload_File = models.FileField()##### don't touch!

 
