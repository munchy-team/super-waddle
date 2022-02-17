from django.db import models

class Availability(models.Model):
  ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
  yesno = (
     ('Yes', 'Yes'),
     ('No', 'No'),
    # ('test', 'test'),
      )
  Name = models.CharField(max_length=5, choices=ppl)
  Available = models.CharField(max_length=5, choices=yesno)
  On_Docs = models.CharField(max_length=5, choices=yesno)
  Notes = models.CharField(max_length=250,blank=True)
  Updated_At = models.TimeField(blank=True, null=True)

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



class Assignment(models.Model):
  Name_Of_Assignment = models.CharField(max_length=150)
  Date_Assigned = models.DateTimeField()
  ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
  Assigned_By = models.CharField(max_length=5, choices=ppl)
  Primary_Assigned_Person = models.CharField(max_length=5,choices=ppl)
  Secondary_Assigned_Person = models.CharField(max_length=5,choices=ppl, blank=True)
  Tertiary_Assigned_Person = models.CharField(max_length=5,choices=ppl, blank=True)  
  Task = models.CharField(max_length=250, blank=True)
  Due_Date = models.DateField()
  Description = models.TextField(max_length=1000, blank=True)
  Link = models.URLField(max_length=2000, blank=True)
  Optional_Link_1 = models.URLField(max_length=2000, blank=True)
  Optional_Link_2 = models.URLField(max_length=2000, blank=True)
  Optional_Link_3 = models.URLField(max_length=2000, blank=True)
  res_choices = (
    ('Not Yet', 'Not Yet'),
    ('Yes', 'Yes'),
    ('Postponed', 'Postponed'),
   # ('bye bye bye', 'gone'),
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
  From = models.CharField(max_length=5, choices=ppl, blank=True)
  To = models.CharField(max_length=5, choices=ppl, blank=True)
  #name = models.CharField(max_length=200)
  date = models.DateTimeField(null=True, blank=True)
  Message = models.TextField(max_length=700)
  #Time = models.DateTimeField()
  #To = models.CharField(choices=ppl, max_length=100)
 # Subject = models.CharField(max_length=250,  blank=True)
 # Message = models.CharField(max_length=500)
 # From = models.CharField(max_length=100, choices=ppl)
 # Response = models.CharField(max_length=500,blank=True)
 # Response_From = models.CharField(max_length=10, choices=ppl,default='test')
 # Time_Of_Response = models.TimeField(null=True, blank=True)

class File_Upload_Center(models.Model):
  Time = models.DateTimeField()
  File_Name = models.CharField(max_length=250)
  Upload_File = models.FileField()
  Description = models.TextField(max_length=250)