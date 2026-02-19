from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from .models import Recipe
# Create your views here.
class RecipeListView(TemplateView):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    def get_context_data(self, **kwargs):
        return ctx

class RecipeInfoView(TemplateView):
    template_name = 'ledger/recipe_info.html'

    def get_context_data(self, **kwargs):
        recipe_id = int(self.kwargs.get('recipe_id')) - 1
        return ctx['recipes'][recipe_id]
