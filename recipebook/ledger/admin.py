"""Main admin panel for ledger project."""
from django.contrib import admin
from .models import Recipe, RecipeIngredient
# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    """Inline class for RecipeIngredient in admin panel."""

    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    """Settings for how recipes will be displayed in RecipeAdmin."""

    model = Recipe
    inlines = [RecipeIngredientInline,]


admin.site.register(Recipe, RecipeAdmin)
