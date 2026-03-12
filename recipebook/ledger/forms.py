"""Forms for ledger app."""
from django import forms
from .models import RecipeImage, Recipe


class RecipeForm(forms.ModelForm):
    """Form for creating new recipes."""
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeImageForm(forms.ModelForm):
    """Form for uploading images for recipes."""
    class Meta:
        model = RecipeImage
        fields = '__all__'
