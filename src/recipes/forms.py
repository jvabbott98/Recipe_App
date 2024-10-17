from django import forms

CHART__CHOICES = (        
   ('#1', 'Number of ingredients'),   
   ('#2', 'Difficulty'),
   ('#3', 'Cooking Time')
   )

class IngredientSearchForm(forms.Form):
    ingredient_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
            'class': 'form-control',  
            'placeholder': 'Enter an ingredient',  
        })
    )

class DataVisualization(forms.Form):
    ingredient_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={
            'class': 'form-control',  
            'placeholder': 'Enter an ingredient',  
        })
    )
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)