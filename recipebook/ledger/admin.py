"""Main admin panel for ledger project."""
from django.contrib import admin
from .models import Recipe, RecipeIngredient, Profile, RecipeImage
# Register your models here.


class RecipeIngredientInline(admin.TabularInline):
    """Inline class for RecipeIngredient in admin panel."""

    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    """Inline class for RecipeImage in admin panel."""

    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    """Settings for how recipes will be displayed in RecipeAdmin."""

    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInline]


class ProfileAdmin(admin.ModelAdmin):
    """Admin panel for profile."""
    model = Profile


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile, ProfileAdmin)
