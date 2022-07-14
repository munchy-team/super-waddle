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
    Notes = models.TextField(blank=True, max_length=5000)


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

    div_class = models.CharField(blank=True, max_length=250, help_text='List the classes for the div for the main banner background. THIS WILL ONLY WORK FOR THE INFO BANNER.')
    style = models.TextField(blank=True, max_length=1000, help_text='List the style for the div for the main banner background. THIS WILL ONLY WORK FOR THE INFO BANNER.')
    Notes = models.TextField(blank=True, max_length=5000)


class Economy(models.Model):
    H1_Heading = models.CharField(blank=True, max_length=23, help_text='There can only be one heading. This is the main heading on banner on the homepage')
    MCI = models.CharField(blank=True, max_length=10, help_text='This should be a number for MCI.')
    AMG = models.CharField(blank=True, max_length=10, help_text='This should be a number for AMG.')
    Button1 = models.CharField(blank=True, max_length=300, help_text='This will the name for the first button on the economy banner on the homepage.')
    Hyperlink_of_Button1 = models.CharField(blank=True, max_length=7000, help_text='This is the hyperlink for button 1. Please include "https://" and the full link for the button.')
    Small_Text_1 = models.CharField(blank=True, max_length=500, help_text='The small text in the economy banner')
    Small_Text_2 = models.CharField(blank=True, max_length=500, help_text='The small text in the economy banner')
    Small_Text_3 = models.CharField(blank=True, max_length=500, help_text='The small text in the economy banner')
    Small_Text_3 = models.CharField(blank=True, max_length=500, help_text='The small text in the economy banner')
    div_class = models.CharField(blank=True, max_length=250, help_text='List the classes for the div for the main banner background. THIS WILL ONLY WORK FOR THE MUNCHYWAR ECONOMY BANNER.')
    style = models.TextField(blank=True, max_length=1000, help_text='List the style for the div for the main banner background.THIS WILL ONLY WORK FOR THE MUNCHYWAR ECONOMY BANNER. ')
    Notes = models.TextField(blank=True, max_length=5000)


class BannerBackground(models.Model):
    div_class = models.CharField(blank=True, max_length=250, help_text='List the classes for the div for the main banner background. THIS WILL ONLY WORK FOR THE MAIN BANNER.')
    style = models.TextField(blank=True, max_length=1000, help_text='List the style for the div for the main banner background.THIS WILL ONLY WORK FOR THE MAIN BANNER.')
    div_class_info_banner = models.CharField(blank=True, max_length=250, help_text='List the classes for the div for the main banner background. THIS WILL ONLY WORK FOR THE MAIN BANNER.')
    style_info_banner = models.TextField(blank=True, max_length=1000, help_text='List the style for the div for the main banner background.THIS WILL ONLY WORK FOR THE MAIN BANNER.')
    Notes = models.TextField(blank=True, max_length=5000)


