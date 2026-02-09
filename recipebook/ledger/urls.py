from django.urls import path
from .views import RecipeListView, RecipeInfoView

urlpatterns = [
    path('list', RecipeListView.as_view(), name='recipe-list'),
    path('<int:recipe_id>', RecipeInfoView.as_view(), name='recipe-info')
]