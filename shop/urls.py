from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search, name="search"),
    path("<str:name>/", views.category_detail, name="category_detail"),
    path("<str:category_name>/product/<int:pk>/", views.product_detail, name="product_detail")
]
