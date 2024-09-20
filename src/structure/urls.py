from django.urls import path

from src.structure.views import *

urlpatterns = [
    path("category/", CategoryListAPIView.as_view()),
    path("category/create/", CategoryCreateAPI.as_view()),
    path("category/<int:category_id>/", CategoryDetailView.as_view()),
]
