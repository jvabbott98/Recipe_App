# Generated by Django 5.1.1 on 2024-09-27 05:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('recipes', '0002_recipe_author_recipe_cuisine_recipe_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authors.author'),
        ),
    ]
