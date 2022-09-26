from django.urls import path
from recipe.api.views import getRecipes
urlpatterns = [
    path('',getRecipes.as_view()),
]