from django.db import models
import uuid

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_password = models.CharField(max_length=30)
    user_email = models.EmailField(max_length=45, null=True, blank=True)

class Well_Being(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    height=models.DecimalField(max_digits=4, decimal_places=1)
    weight=models.DecimalField(max_digits=4, decimal_places=1)
    target_weight=models.DecimalField(max_digits=4, decimal_places=1)
    birthday=models.DateTimeField
    age=models.IntegerField
    ddl=models.DateTimeField(blank=True, null=True)

class Nutrients(models.Model):
    User_id=models.OneToOneField(User,on_delete=models.CASCADE)
    calorie=models.IntegerField
    carbs=models.IntegerField
    fat=models.IntegerField
    protein=models.IntegerField

class Ingredients(models.Model):
    Ingredients_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    calorie = models.IntegerField
    carbs = models.IntegerField
    fat = models.IntegerField
    protein = models.IntegerField
    img_url = models.URLField

class Recipes(models.Model):
    Recipes_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    update_time = models.DateTimeField

class Like_Food(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField

class Dislike_Food(models.Model):
    User_id = models.OneToOneField(User, on_delete=models.CASCADE)
    Ingredients_id = models.OneToOneField(Ingredients, on_delete=models.CASCADE)
    update_time = models.DateTimeField
