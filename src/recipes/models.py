from django.db import models
from ingredients.models import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=120)

    cooking_time = models.IntegerField(help_text='In minutes')

    ingredients = models.ManyToManyField(Ingredient)
