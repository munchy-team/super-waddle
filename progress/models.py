from django.db import models

class Progresse(models.Model):
  name = models.CharField(max_length=255)
  date = models.DateTimeField()
  Notes = models.TextField(max_length=7500, blank=True)

class VisualStudioCodeLink(models.Model):
  Title = models.CharField(max_length=250)
  Date = models.DateTimeField()
  Link = models.URLField(max_length=1000, blank=True)

class WebsiteIdea(models.Model):
  Website_Idea = models.CharField(max_length=250)
  Date = models.DateTimeField()
  Describe_Your_Idea = models.TextField(max_length=500)

class Excel(models.Model):
  Title = models.CharField(max_length=250)
  Date = models.DateTimeField()
  Link = models.URLField(max_length=1000, blank=True)

class Contact(models.Model):
  Name = models.CharField(max_length=250)
  Date = models.DateTimeField()
  Link = models.URLField(max_length=1000, blank=True)

  

# Create your models here.
