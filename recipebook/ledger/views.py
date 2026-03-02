"""Module that lists views of ledger app."""
from django.views.generic import TemplateView
from .models import Recipe, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
# Create your views here.


class RecipeListView(TemplateView):
    """View to list all recipes."""

    template_name = "ledger/recipe_list.html"

    def get_context_data(self, **kwargs):
        """Get context data."""
        ctx = super().get_context_data(**kwargs)
        ctx["recipes"] = Recipe.objects.all()
        ctx["page_name"] = "Recipe List"
        return ctx


class RecipeInfoView(LoginRequiredMixin, TemplateView):
    """View to show info per recipe."""

    template_name = 'ledger/recipe_info.html'
    login_url = '/accounts/login/'
    def get_context_data(self, **kwargs):
        """Get context data."""
        ctx = super().get_context_data(**kwargs)
        recipe_id = int(self.kwargs.get('pk'))
        recipe_name = Recipe.objects.filter(pk=recipe_id).first().name
        ingredients = RecipeIngredient.objects.filter(
            corresponding_recipe__name=recipe_name
        )
        ctx["page_name"] = "Recipe Info"
        ctx['ingredients'] = [
            {"quantity": ri.quantity, "name": ri.corresponding_ingredient.name}
            for ri in ingredients
        ]
        ctx['name'] = recipe_name
        ctx['author_name'] = Recipe.objects.filter(pk=recipe_id).first().author.name
        return ctx
