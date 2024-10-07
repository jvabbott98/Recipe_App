from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Recipe


# class RecipeListView(ListView):
#     model = Recipe
#     template_name = 'recipes/main.html'

def recipe_list(request):
    object_list = Recipe.objects.all()
    return render(request, 'recipes/main.html', {'object_list': object_list})

def recipe_detail(request, pk):
    object = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/detail.html', {'object': object})

def home(request):
    return render(request, 'recipes/recipes_home.html')
