# Generated by Django 4.0 on 2022-10-28 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recipes', '0001_initial'),
        ('favoriterecipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='favoriterecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_favorite_recipes', to='recipes.recipes'),
        ),
    ]
