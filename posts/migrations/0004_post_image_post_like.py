# Generated by Django 4.2.1 on 2023-05-31 01:33

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_body_post_created_at_post_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.IntegerField(blank=True, default=0, verbose_name='like'),
        ),
    ]
