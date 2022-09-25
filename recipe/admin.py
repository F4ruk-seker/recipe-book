from django.contrib import admin
from recipe.models import material
from recipe.models import Recipe
from recipe.models import recipeTag

# Register your models here.
admin.site.register(material)
admin.site.register(Recipe)
admin.site.register(recipeTag)