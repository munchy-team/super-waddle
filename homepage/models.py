from django.db import models

# Create your models here.

class Banner(models.Model):
    H1_Heading = models.CharField(blank=True, max_length=36, help_text='There can only be one heading. This is the main heading on banner on the homepage')
    Paragraph = models.CharField(blank=True, max_length=250, help_text='There can only be one paragraph. This is the main paragraph on banner on the homepage')
    Link_or_Button_Name_For_Button_1 =models.CharField(blank=True, max_length=20, help_text='This will the name for the first button on the banner on the homepage.')
    Hyperlink_of_Button1 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 1. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_2 =models.CharField(blank=True, max_length=20, help_text='This will the name for the second button on the banner on the homepage.')
    Hyperlink_of_Button2 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 2. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_3 =models.CharField(blank=True, max_length=20, help_text='This will the name for the third button on the banner on the homepage.')
    Hyperlink_of_Button3 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 3. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_4 =models.CharField(blank=True, max_length=20, help_text='This will the name for the fourth button on the banner on the homepage.')
    Hyperlink_of_Button4 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 4. Please include "https://" and the full link for the button.')


class AdminBanner(models.Model):
    H1_Heading = models.CharField(blank=True, max_length=36, help_text='There can only be one heading. This is the main heading on banner on the homepage')
    Paragraph = models.CharField(blank=True, max_length=250, help_text='There can only be one paragraph. This is the main paragraph on banner on the homepage')
    Link_or_Button_Name_For_Button_1 =models.CharField(blank=True, max_length=20, help_text='This will the name for the first button on the banner on the homepage.')
    Hyperlink_of_Button1 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 1. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_2 =models.CharField(blank=True, max_length=20, help_text='This will the name for the second button on the banner on the homepage.')
    Hyperlink_of_Button2 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 2. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_3 =models.CharField(blank=True, max_length=20, help_text='This will the name for the third button on the banner on the homepage.')
    Hyperlink_of_Button3 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 3. Please include "https://" and the full link for the button.')

    Link_or_Button_Name_For_Button_4 =models.CharField(blank=True, max_length=20, help_text='This will the name for the fourth button on the banner on the homepage.')
    Hyperlink_of_Button4 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 4. Please include "https://" and the full link for the button.')
