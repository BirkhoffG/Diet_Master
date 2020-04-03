from django.contrib import admin
from .models import *


# Register your models here.
models = [WellBeing, Nutrients, Ingredients, Recipes, LikeFood, DislikeFood]
admin.site.register(models)
