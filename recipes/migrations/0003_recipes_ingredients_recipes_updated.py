# Generated by Django 4.0 on 2022-03-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='ingredients',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='recipes',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
