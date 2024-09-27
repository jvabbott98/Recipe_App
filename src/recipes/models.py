from django.db import models
from ingredients.models import Ingredient
from authors.models import Author
from cuisines.models import Cuisine
from django.db.models.signals import post_save
from django.dispatch import receiver

class Recipe(models.Model):
    name = models.CharField(max_length=120)

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    cooking_time = models.IntegerField(help_text='In minutes')

    description = models.TextField(default='No description...')
    directions = models.TextField(default='No directions....')

    ingredients = models.ManyToManyField(Ingredient, related_name='ingredients')
    cuisine = models.ManyToManyField(Cuisine, related_name='cuisine')


    difficulty = models.CharField(max_length=20, blank=True)

    


    def calculate_difficulty(self):
        ingredient_count = self.ingredients.count()
        if self.cooking_time < 10:
            if ingredient_count < 4:
                return 'Easy'
            else:
                return 'Medium'
        else:
            if ingredient_count < 4:
                return 'Intermediate'
            else:
                return 'Hard'

    def __str__(self):
        return str(self.name)

@receiver(post_save, sender=Recipe)
def set_difficulty(sender, instance, created, **kwargs):
    if created:  
        instance.difficulty = instance.calculate_difficulty()
        instance.save(update_fields=['difficulty']) 