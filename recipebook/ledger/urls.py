"""File that lists ledger app's valid urls."""
from django.urls import path
from .views import RecipeListView, RecipeInfoView, RecipeAddView, RecipeAddImageView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipe-list'),
    path('recipe/<int:pk>', RecipeInfoView.as_view(), name='recipe-info'),
    path('recipe/add', RecipeAddView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/add_image', RecipeAddImageView.as_view(), name='recipe-add-image'),
]
