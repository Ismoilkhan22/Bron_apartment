from django.urls import path

from src.structure.views import *

urlpatterns = [
    # category api  urls
    path("category/", CategoryListAPIView.as_view()),
    path("category/create/", CategoryCreateAPI.as_view()),
    path("category/<int:category_id>/", CategoryDetailView.as_view()),

    # product_rule api urls
    path("product_rule/", ProductRuleListAPIView.as_view()),
    path("product_rule/<int:pk>/", ProductRuleDetailAPIView.as_view()),

    # comfort api urls
    path("comfort/", ComfortListAPIView.as_view()),
    path("comfort/<int:pk>/",ComfortDetailAPIView.as_view()),

    # product image api view
    path("product_image/", ProductImageListAPIView.as_view()),
    path("product_image/<int:pk>/", ProductImageDetailAPIView.as_view()),

    # product api urls
    path("product/", ProductListAPIView.as_view()),
    path("product/<int:pk>/",ProductDetailAPIView.as_view())

]
