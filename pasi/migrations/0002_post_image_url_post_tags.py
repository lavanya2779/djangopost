# Generated by Django 4.2.3 on 2023-07-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
