# Generated by Django 4.2.16 on 2024-11-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0009_blogpost_created_on_alter_blogpost_fun_facts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='habitat',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='species',
            field=models.CharField(blank=True, max_length=85, null=True),
        ),
    ]