# Generated by Django 5.1.1 on 2024-09-27 05:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('cuisines', '0001_initial'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.author', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine',
            field=models.ManyToManyField(to='cuisines.cuisine'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.TextField(default='No description...'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='directions',
            field=models.TextField(default='No directions....'),
        ),
    ]
