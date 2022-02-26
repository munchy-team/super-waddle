# Generated by Django 4.0.2 on 2022-02-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0053_statuse_date_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5)),
                ('To', models.CharField(blank=True, choices=[('test', 'test'), ('C,H', 'C,H'), ('S,A', 'S,A'), ('S,L', 'S,L')], max_length=5)),
                ('Posted_At', models.DateTimeField(blank=True, null=True)),
                ('Message', models.TextField(max_length=700)),
            ],
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
