# Generated by Django 4.2.16 on 2024-11-24 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0007_blogpost_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
