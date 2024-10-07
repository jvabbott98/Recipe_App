from django.urls import path
from .views import home, recipe_list, recipe_detail

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('recipes/', recipe_list, name='recipes'),
    path('recipes/<pk>', recipe_detail, name='detail')
]