from django.shortcuts import render
from shop.models import Product


def homepage_view(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})

