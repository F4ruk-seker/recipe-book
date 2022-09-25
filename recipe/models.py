from django.db import models
from django.db.models import Q,Sum

from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
# Create your models here.
class Recipe(models.Model):
    title = models.TextField(max_length=150,default=None)
    createBy = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    how_make = RichTextField(default=None)
    materialList = models.ManyToManyField('material',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    recipe_tag = models.ManyToManyField('recipeTag',blank=True)

    def getTags(self):
        return self.recipe_tag.values()
    def getColire(self):
        return self.materialList.aggregate(Sum('calorie'))

    def __str__(self):
        return f"{self.title} - {self.created}"

class recipeTag(models.Model):
    name = models.TextField()


class material(models.Model):
    name = models.TextField()
    calorie = models.IntegerField()
    quantity = models.IntegerField()