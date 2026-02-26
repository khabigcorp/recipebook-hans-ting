"""File that lists ledger app's valid urls."""
from django.urls import path
from .views import RecipeListView, RecipeInfoView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeInfoView.as_view(), name='recipe-info')
]
