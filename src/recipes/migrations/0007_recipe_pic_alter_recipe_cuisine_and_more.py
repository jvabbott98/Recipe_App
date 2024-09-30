# Generated by Django 5.1.1 on 2024-09-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisines', '0001_initial'),
        ('ingredients', '0001_initial'),
        ('recipes', '0006_recipe_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='books'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.ManyToManyField(related_name='cuisine', to='cuisines.cuisine'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', to='ingredients.ingredient'),
        ),
    ]
