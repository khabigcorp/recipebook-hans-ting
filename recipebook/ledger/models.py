"""File that stores models of ledger app."""
from django.db import models
from django.urls import reverse
# Create your models here.


class Ingredient(models.Model):
    """Ingredient class that represents recipe ingredients."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Return string version of Ingredient."""
        return self.name

    def get_absolute_url(self):
        """Get url to Ingredient object."""
        return reverse("ledger:recipe-info", kwargs={"recipe_id": self.pk})


class Recipe(models.Model):
    """Recipe class that represents recipes."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Return string version of Recipe."""
        return self.name

    def get_absolute_url(self):
        """Get url to Recipe object."""
        return reverse("ledger:recipe-info", kwargs={"recipe_id": self.pk})


class RecipeIngredient(models.Model):
    """Associative object allowing for recipe-ingredient lookup."""

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    corresponding_ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipes'
    )
    corresponding_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )
