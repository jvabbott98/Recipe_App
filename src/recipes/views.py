from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Recipe



def recipe_list(request):
    object_list = Recipe.objects.all()
    return render(request, 'recipes/main.html', {'object_list': object_list})

def recipe_detail(request, id):
    object = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'object': object})

def home(request):
    return render(request, 'recipes/recipes_home.html')
