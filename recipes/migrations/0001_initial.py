# Generated by Django 4.0 on 2022-10-28 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uploadfile', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('ingredients', models.TextField(blank=True)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.categories')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uploadfile.uploadfile')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
