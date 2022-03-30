# Generated by Django 3.1.4 on 2022-03-19 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('munchyblog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homeblog',
            old_name='Second_Paragraph',
            new_name='IntroParagraph',
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem4',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem5',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem6',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem7',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem8',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='ListItem9',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='homeblog',
            name='SecondParagraph',
            field=models.TextField(blank=True, max_length='500'),
        ),
    ]