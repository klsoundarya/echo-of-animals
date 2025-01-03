# Generated by Django 4.2.16 on 2024-11-27 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('echoes', '0004_blogpost_diet'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact_text', models.TextField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='facts', to='echoes.blogpost')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='fun_facts',
            field=models.ManyToManyField(blank=True, related_name='blog_posts_facts', to='echoes.animalfact'),
        ),
    ]
