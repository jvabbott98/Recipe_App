from django.db import models
from ingredients.models import Ingredient

class Recipe(models.Model):
    name = models.CharField(max_length=120)

    cooking_time = models.IntegerField(help_text='In minutes')

    ingredients = models.ManyToManyField(Ingredient)

    pic = models.ImageField(upload_to='books', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
