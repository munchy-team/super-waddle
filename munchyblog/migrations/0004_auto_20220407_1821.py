# Generated by Django 3.1.4 on 2022-04-07 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munchyblog', '0003_auto_20220318_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeblog',
            name='Author',
            field=models.CharField(blank=True, choices=[('MunchyTeam Moderator', 'MunchyTeam Moderator'), ('AS', 'AS'), ('Calvin', 'Calvin'), ('LS', 'LS'), ('Hudson Crisp', 'Hudson Crisp')], max_length=30),
        ),
        migrations.AlterField(
            model_name='homeblog',
            name='Post_Author_MunchySite_Admin_Purposes_Only',
            field=models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L'), ('C,G', 'C,G')], max_length=5),
        ),
    ]