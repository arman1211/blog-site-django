# Generated by Django 5.0.6 on 2024-06-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catagory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
