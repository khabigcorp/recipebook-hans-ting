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
        recipe_name = Recipe.objects.filter(pk=recipe_id).first().name
        ingredients = RecipeIngredient.objects.filter(corresponding_recipe__name=recipe_name)

        ctx['ingredients'] = [{"quantity": ri.quantity, "name": ri.corresponding_ingredient.name} for ri in ingredients]
        ctx['name'] = recipe_name
        return ctx
