from django.db import models

class Progresse(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateField()
  Notes = models.TextField(max_length=7500, blank=True)
  

# Create your models here.
