from django.shortcuts import render

from recipe.models import Recipe
from recipe.models import material
# Create your views here.
def mainPage(request):
    Recipe_all = Recipe.objects.all()

    return render(request,'index.html',context={
        'recipe_all':Recipe_all
    })

def getRecipe():
    material.objects.all().order_by('--id')
    return