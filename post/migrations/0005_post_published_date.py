# Generated by Django 5.0.6 on 2024-06-06 07:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateField(default=datetime.datetime(2024, 6, 6, 13, 58, 51, 69360)),
        ),
    ]
