from django.db import models

# Create your models here.
class HomeBlog(models.Model):
    Post_Title = models.CharField(max_length=200)
    Date = models.DateTimeField()
    mod = (
        ('MunchyTeam Moderator', 'MunchyTeam Moderator'),
        ('AS','AS'),
        ('Calvin','Calvin'),
        ('LS', 'LS'),
        ('Hudson Crisp','Hudson Crisp'),
        ('Carson','Carson'),
        ('MunchyBlog Author','MunchyBlog Author'),


        )
    Author = models.CharField(choices=mod, max_length=30)
   
    users = (
      ('test','test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      ('C,G', 'C,G'),
      ('Other','Other'),
      )
    Post_Author_MunchySite_Admin_Purposes_Only = models.CharField(max_length=5, blank=True, choices=users)
    IntroParagraph = models.TextField(max_length="1000", blank=True)
    Header1 = models.CharField(max_length=100, blank=True)
    Paragraph1 = models.TextField(max_length="1000", blank=True)
    SecondParagraph = models.TextField(max_length="1000", blank=True)
    Header2 = models.CharField(max_length=100, blank=True)
    Paragraph2 = models.TextField(max_length="1000", blank=True)
    Header2_Second_Paragraph = models.TextField(max_length="1000", blank=True)
    Header3 = models.CharField(max_length=100, blank=True)
    Paragraph3 = models.TextField(max_length="1000", blank=True)
    Header3_Second_Paragraph = models.TextField(max_length="1000", blank=True)
    ListItem1 = models.CharField(max_length=100, blank=True)
    ListItem2 = models.CharField(max_length=100, blank=True)
    ListItem3 = models.CharField(max_length=100, blank=True)
    ListItem4 = models.CharField(max_length=100, blank=True)
    ListItem5 = models.CharField(max_length=100, blank=True)
    ListItem6 = models.CharField(max_length=100, blank=True)
    ListItem7 = models.CharField(max_length=100, blank=True)
    ListItem8 = models.CharField(max_length=100, blank=True)
    ListItem9 = models.CharField(max_length=100, blank=True)
   # Embeded = models.CharField(max_length=1000, blank=True)
