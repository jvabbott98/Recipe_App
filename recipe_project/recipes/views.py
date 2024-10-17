from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import IngredientSearchForm, DataVisualization
from .models import Ingredient, Recipe
import pandas as pd
from .utils import get_chart
from django.db.models import Count

@login_required
def recipe_list(request):
    form = IngredientSearchForm() 
    qs = Recipe.objects.annotate(number_of_ingredients=Count('ingredients'))  # Annotate all recipes
    recipes_df = None  
    object_list = qs  # Default to showing all recipes


    if request.method == 'POST':
        


        if 'view_all' in request.POST:
                # Return all recipes
                object_list = qs 
        else:
            form = IngredientSearchForm(request.POST)


            if form.is_valid():
                # Handle the "View All Recipes" case
                if 'view_all' in request.POST:
                    # Return all recipes
                    object_list = qs 
                else:
                    # Handle ingredient search
                    ingredient_name = form.cleaned_data['ingredient_name']
                    object_list = qs.filter(ingredients__name__icontains=ingredient_name)

            else:
                # Handle form errors if necessary
                print("Form is not valid:", form.errors)

    context = {
        'form': form,
        'object_list': object_list,
    }

    return render(request, 'recipes/main.html', context)

@login_required
def visualization(request):
    form = DataVisualization() 
    recipes_df = None
    chart = None
    qs = Recipe.objects.annotate(number_of_ingredients=Count('ingredients'))
    object_list = qs

    if request.method == 'POST':
        form = DataVisualization(request.POST)

        if form.is_valid():
            chart_type = form.cleaned_data['chart_type']
            ingredient_name = request.POST.get('ingredient_name')
            qs = qs.filter(ingredients__name__icontains=ingredient_name)
            object_list = qs

            recipes_df = pd.DataFrame(object_list.values('name', 'cooking_time', 'difficulty', 'number_of_ingredients'))

            if not recipes_df.empty:
                difficulty_counts = recipes_df['difficulty'].value_counts().to_list()
                difficulty_labels = recipes_df['difficulty'].value_counts().index.tolist()

                chart = get_chart(chart_type, recipes_df, difficulty_levels=difficulty_labels, difficulty_counts=difficulty_counts)
                recipes_df = recipes_df.to_html()
        else:
            print("Form is not valid:", form.errors)

    context = {
        'form': form,
        'recipes_df': recipes_df,
        'chart': chart,
        'object_list': object_list,
    }

    return render(request, 'recipes/visualization.html', context)


@login_required
def recipe_detail(request, id):
    object = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'object': object})

def home(request):
    return render(request, 'recipes/recipes_home.html')
