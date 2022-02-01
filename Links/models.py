from django.db import models

# Create your models here.

class Link(models.Model):
  Time: models.DateTimeField
  Link_Name: models.CharField(max_length=250)
  URL: models.URLField(max_length=7501)
  

