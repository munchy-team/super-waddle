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
  res_choices = (
    ('Not Yet', 'Not Yet'),
    ('Yes', 'Yes'),
    ('Postponed', 'Postponed'),
    ('Out The Window!(Canceled)',  'Out The Window!(Canceled)'))
  Resolved = models.CharField(max_length=30, choices=res_choices)
  # it does not work. 
  Latest_Important_Message = models.CharField(max_length=100, blank=True)
  Message_Posted_At = models.TimeField(blank=True, null=True)
  Less_Important_Messages_And_Chat = models.TextField(blank=True, max_length=5000)  

class Messages(models.Model):
  ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
  Time = models.DateTimeField()
  To = models.CharField(choices=ppl, max_length=250)
  Subject = models.CharField(max_length=250,  blank=True)
  Message = models.CharField(max_length=250)
  Response = models.CharField(max_length=250,default="Type your response here.")
  From = models.CharField(max_length=250, choices=ppl)

#class Special_Messages(models.Model):
   # ppl = (
     #('test', 'test'),
      #('C,H', 'C,H'),
      #('S,A', 'S,A'),
      #('S,L', 'S,L'),
      #)
    #To = models.CharField(max_length=250)
  #  Date = models.DateTimeField()
   # Link = models.URLField(max_length=1000, blank=True)
  #class links(models.Model)