# Generated by Django 4.0 on 2022-01-30 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='favorite_recipes',
            field=models.ManyToManyField(through='favoriterecipe.FavoriteRecipe', to='recipes.Recipes'),
        ),
    ]
