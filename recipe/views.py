from django.shortcuts import render
from django.shortcuts import redirect

from recipe.models import Recipe, recipeTag
from recipe.models import material

from recipe.forms import recipeForm
def mainPage(request):
    Recipe_all = Recipe.objects.all()

    recipe_basis = recipeForm(request.POST or None)
    if recipe_basis.is_valid():
        recipe_basis_data = recipe_basis.save(commit=False)
        recipe_basis_data.createBy = request.user

        # recipe_basis_data.how_make = reMakeTextToHtml(recipe_basis_data.how_make)

        default_image = 'https://firebasestorage.googleapis.com/v0/b/otomation-b0c8a.appspot.com/o/userAvatars%2Fdefault.jpg?alt=media&token=f82a1c8b-542b-45a2-91b5-03a0a8cc6650'

        if not request.POST.get('image'):
            recipe_basis_data.image = default_image

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

def reMakeTextToHtml(text:str):
    data = text.split(" ")
    count = 0
    titles = ['#','#'*2,'#'*3,'#'*4,'#'*5,'#'*6]

    def getNextOrFalse(index):
        try:
            return data[index+1]
        except:
            return False
    for let in data:
        if let in titles:
            if getNextOrFalse(count):
                size = len(let)
                data[count] = f"<h{size}>{data[count+1]}</h{size}>"
                data.pop(count)

        if let == '*':
            if getNextOrFalse(count):
                data[count+1] = f"<p class='recipe_list'>{data[count+1]}</p>"
                data.pop(count)
        count += 1

    return "".join(data)