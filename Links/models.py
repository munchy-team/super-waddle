from django.db import models

# Create your models here.

class Link(models.Model):
  Time = models.DateTimeField(null=True)
  Link_Name = models.CharField(max_length=250)
  URL = models.URLField(max_length=7501, null=True)
  Munchy_ID = models.CharField(max_length=70, null=True)
# you need to reconnect the repo to heroku. 
# hello are you back?