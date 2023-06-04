from django.urls import path
from . import views

urlpatterns = [
    path("search/", views.search, name="search"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("change_quantity/<int:product_id>/", views.change_quantity, name="change_quantity"),
    path("remove_from_cart/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart/payment/", views.payment, name="payment"),
    path("order_history/", views.order_history, name="order_history"),
    path("<str:name>/", views.category_detail, name="category_detail"),
    path("<str:category_name>/product/<int:pk>/", views.product_detail, name="product_detail"),
]
