from django.test import TestCase
from .models import Recipe
from ingredients.models import Ingredient

class RecipeModelTests(TestCase):
    def test_create_recipe(self):
        recipe = Recipe.objects.create(name="Tea", cooking_time = 5)
        self.assertEqual(recipe.name, "Tea")
        self.assertEqual(recipe.cooking_time, 5)

    def test_retrieve_ingredients_from_recipe(self):
        recipe = Recipe.objects.create(name="Tea", cooking_time = 5)
        ingredient = Ingredient.objects.create(name="Water")

        recipe.ingredients.add(ingredient)

        retrieved_recipe = Recipe.objects.get(name = "Tea")
        self.assertEqual(retrieved_recipe.ingredients.first(), ingredient)

    def test_cooking_time_positive(self):
        recipe = Recipe.objects.create(name="Tea", cooking_time = -10)
        self.assertLess(recipe.cooking_time, 0)  



