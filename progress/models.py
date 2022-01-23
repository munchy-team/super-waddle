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

class Assignment(models.Model):
  Name_Of_Assignment = models.CharField(max_length=50)
  Date_Assigned = models.DateTimeField()
  ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
  Assigned_To = models.CharField(max_length=5,choices=ppl)
  Assigned_By = models.CharField(max_length=5, choices=ppl)
  Task = models.CharField(max_length=250)
  Due_Date = models.DateField()
  Description = models.TextField(max_length=1000)
  Link = models.URLField(max_length=2000)
  Optional_Link = models.URLField(max_length=2000, blank=True)
  Optional_Link = models.URLField(max_length=2000, blank=True)
  Optional_Link = models.URLField(max_length=2000, blank=True)
  

# Create your models here.
