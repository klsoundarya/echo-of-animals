# Generated by Django 4.2.16 on 2024-11-27 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0006_funfactslider'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='intro',
            field=models.TextField(blank=True),
        ),
    ]
