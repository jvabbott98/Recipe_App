from django import forms

CHART__CHOICES = (        
   ('#1', 'Number of ingredients'),   
   ('#2', 'Difficulty'),
   ('#3', 'Cooking Time')
   )

class IngredientSearchForm(forms.Form):
    ingredient_name = forms.CharField(max_length=120)

class ChartChoices(forms.Form):
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)