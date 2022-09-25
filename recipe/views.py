from django.shortcuts import render
from django.shortcuts import redirect

from recipe.models import Recipe, recipeTag
from recipe.models import material

from recipe.forms import recipeForm
def mainPage(request):
    Recipe_all = Recipe.objects.all()
    new_recipe_form = recipeForm
    recipe_basis = new_recipe_form(request.POST or None)
    if recipe_basis.is_valid():
        recipe_basis_data = recipe_basis.save(commit=False)
        recipe_basis_data.createBy = request.user

        recipe_basis_data.save()

        recipeTagList = request.POST.getlist('recipe_tag')

        for tag in recipeTagList:
            recipe_basis_data.recipe_tag.add(tag)

        material_names = request.POST.getlist('material_name')

        material_quantitys = request.POST.getlist('material_quantity')
        material_calorie = request.POST.getlist('material_calorie')

        for material_input_index in range(len(material_names)):

            if material_names[material_input_index]:

                _material = material.objects.create(
                    name=material_names[material_input_index],
                    calorie=int(material_quantitys[material_input_index] or 0),
                    quantity=int(material_calorie[material_input_index] or 0))

                recipe_basis_data.materialList.add(_material)
        return redirect('main_page')

    return render(request,'index.html',context={
        'recipe_all':Recipe_all,
        'new_recipe_form':recipe_basis
    })

def getRecipe():
    material.objects.all().order_by('--id')
    return

def getTagIdFromNumber(number):
    try:
        return recipeTag.objects.get(id=number)
    except:
        return False