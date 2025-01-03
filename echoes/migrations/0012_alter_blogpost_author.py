# Generated by Django 4.2.16 on 2024-11-28 02:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('echoes', '0011_guestuser_blogpost_guest_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animal_blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
