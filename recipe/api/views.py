from rest_framework.filters import SearchFilter

from rest_framework.generics import ListAPIView

from recipe.models import Recipe

from recipe.api.serializers import RecipeSerializer
class getRecipes(ListAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    filter_backends = [SearchFilter]
    search_fields = ['slug']

    # def get_queryset(self):
    #     return Recipe.objects.all()