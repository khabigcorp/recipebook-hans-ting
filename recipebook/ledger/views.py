from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView
from .models import Recipe, RecipeIngredient
# Create your views here.
class RecipeListView(TemplateView):
    template_name = "ledger/recipe_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["recipes"] = Recipe.objects.all()
        return ctx

class RecipeInfoView(TemplateView):
    template_name = 'ledger/recipe_info.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        recipe_id = int(self.kwargs.get('recipe_id'))
        recipe_title = Recipe.objects.filter(pk=recipe_id).title
        ingredients = RecipeIngredient.objects.filter(corresponding_recipe__title=recipe_title)

        ctx['ingredients'] = ingredients
        ctx['name'] = recipe
        return ctx
