from django.db import models
from django.urls import reverse
# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=[str(self.id)])

class Recipe(models.Model):
    name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tasks:task_detail', args=[str(self.id)])

class RecipeIngredient(models.Model):
    name = models.CharField(max_length = 50)
    quantity = models.IntegerField()
    corresponding_ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
    corresponding_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe'
    )