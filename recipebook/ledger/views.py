"""Module that lists views of ledger app."""
from django.views.generic import TemplateView, CreateView
from .forms import RecipeForm, RecipeImageForm
from .models import Recipe, RecipeIngredient, RecipeImage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
# Create your views here.


class RecipeListView(TemplateView):
    """View to list all recipes."""

    template_name = "ledger/recipe_list.html"

    def get_context_data(self, **kwargs):
        """Get context data."""
        ctx = super().get_context_data(**kwargs)
        ctx["recipes"] = Recipe.objects.all()
        return ctx


class RecipeInfoView(LoginRequiredMixin, TemplateView):
    """View to show info per recipe."""

    template_name = 'ledger/recipe_info.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        """Get context data."""
        ctx = super().get_context_data(**kwargs)
        recipe_id = int(self.kwargs.get('pk'))
        recipe = Recipe.objects.filter(pk=recipe_id).first()
        ingredients = RecipeIngredient.objects.filter(
            corresponding_recipe__name=recipe.name
        )
        images = RecipeImage.objects.filter(
            corresponding_recipe__pk=recipe_id
        )
        ctx['recipe'] = recipe
        ctx['ingredients'] = ingredients
        ctx['images'] = images
        return ctx


class RecipeAddView(LoginRequiredMixin, CreateView):
    """View for adding recipes."""
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_add.html'


class RecipeAddImageView(LoginRequiredMixin, CreateView):
    "View for adding images to recipes."
    model = RecipeImage
    form_class = RecipeImageForm
    template_name = 'ledger/recipe_add_image.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = RecipeImageForm()
        context['pk'] = self.kwargs['pk']
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            return redirect('ledger:recipe-info', pk=image.corresponding_recipe.pk)
