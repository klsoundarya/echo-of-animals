# Generated by Django 4.2.16 on 2024-11-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0005_animalfact_blogpost_fun_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunFactSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_name', models.CharField(max_length=100)),
                ('fact_text', models.TextField()),
                ('image', models.ImageField(upload_to='slider_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
