"""File that stores models of ledger app."""
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.


class Profile(models.Model):
    """Model that represents profiles."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.CharField(validators=[
            MinLengthValidator(
                256,
                message="Must be at least 255 characters long"
            )
        ]
    )


class Ingredient(models.Model):
    """Ingredient class that represents recipe ingredients."""

    name = models.CharField(max_length=50)

    def __str__(self):
        """Return string version of Ingredient."""
        return self.name

    def get_absolute_url(self):
        """Get url to Ingredient object."""
        return reverse("ledger:recipe-info", kwargs={"pk": self.pk})


class Recipe(models.Model):
    """Recipe class that represents recipes."""

    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
        null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return string version of Recipe."""
        return self.name

    def get_absolute_url(self):
        """Get url to Recipe object."""
        return reverse("ledger:recipe-info", kwargs={"pk": self.pk})


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


class RecipeImage(models.Model):
    """Image associated per recipe."""

    image = models.ImageField(
        upload_to='images/',
    )
    description = models.CharField(max_length=255)
    corresponding_recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name = 'images'
    )
