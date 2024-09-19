from django.urls import path

from src.structure.views import CategoryListAPIView

urlpatterns = [
    path("category/list/", CategoryListAPIView.as_view()),
]
