from django import forms
from recipe.models import Recipe

class recipeForm(forms.ModelForm):
    title = forms.CharField(max_length=150)
    how_make = forms.CharField()
    image = forms.CharField(help_text='firebase image | default',required=False)

    class Meta:
        model = Recipe
        fields = ('title','how_make','recipe_tag','image')
