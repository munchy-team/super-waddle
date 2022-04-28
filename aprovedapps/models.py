from django.db import models

# Create your models here.
class MunchyApps(models.Model):
    DateCreated = models.DateField()
    AppName = models.CharField(max_length=500, blank=True)
    Description = models.TextField(max_length=500, blank=True)
    DownloadLink = models.URLField(max_length=5000, blank=True, help_text="This is going to be the link of the publish.htm file on GitHub, or basically the screen where users can click download and the app will be downloaded")
    ppl = (
     ('test', 'test'),
      ('C,H', 'C,H'),
      ('S,A', 'S,A'),
      ('S,L', 'S,L'),
      )
    AppCreator = models.CharField(max_length=5, choices=ppl, blank=True)
