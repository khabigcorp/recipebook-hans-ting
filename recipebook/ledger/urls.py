from django.urls import path
from .views import RecipeListView, RecipeInfoView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:recipe_id>', RecipeInfoView.as_view(), name='recipe-info')
]