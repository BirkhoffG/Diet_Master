from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
# class User(models.Model):
#     user_name = models.CharField(max_length=30)
#     user_password = models.CharField(max_length=30)
#     user_email = models.EmailField(max_length=45, null=True, blank=True)
class AccountAvatar(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar_url = models.CharField(max_length=128)


class WellBeing(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    height = models.DecimalField(max_digits=4, decimal_places=1)
    weight = models.DecimalField(max_digits=4, decimal_places=1)
    target_weight = models.DecimalField(max_digits=4, decimal_places=1)
    birthday = models.DateTimeField()
    gender=models.CharField(max_length=6)
    age = models.IntegerField()
    activity_level = models.DecimalField(max_digits=2, decimal_places=1)
    ddl = models.DateTimeField(blank=True, null=True)


class Nutrients(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    calorie = models.IntegerField(null=True)
    carbon = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)


class Ingredients(models.Model):
    ingredients_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    calorie = models.IntegerField(null=True)
    carbs = models.IntegerField(null=True)
    fat = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)
    img_url = models.URLField(null=True)


class Recipes(models.Model):
    recipes_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    update_time = models.DateTimeField(null=True,auto_now=True)


class LikeFood(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField(null=True,auto_now=True)


class DislikeFood(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField(null=True,auto_now=True)
