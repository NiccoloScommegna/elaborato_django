from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def category_detail(request, name):
    category = get_object_or_404(Category, name=name)
    products = category.products.all()
    return render(request, "category_detail.html", {
        "category": category,
        "products": products
    })


def product_detail(request, category_name, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})
