from django import forms

from .models import RecipeImage, Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'