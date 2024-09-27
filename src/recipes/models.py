from django.db import models
from ingredients.models import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=120)

    cooking_time = models.IntegerField(help_text='In minutes')

    description = models.TextField(default='No description...')
    directions = models.TextField(default='No directions....')

    ingredients = models.ManyToManyField(Ingredient)

    

    

    def calculate_difficulty(self):
        if self.cooking_time < 10:
            if len(self.ingredients) < 4:
                self.difficulty = 'Easy'
            else:
                self.difficulty = 'Medium'
        else:
            if len(self.ingredients)< 4:
                self.difficulty = 'Intermediate'
            else:
                self.difficulty = 'Hard'

    def __str__(self):
        return str(self.name)
