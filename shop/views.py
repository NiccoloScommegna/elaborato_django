from django.shortcuts import render, get_object_or_404
from django.db.models import Q
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


def search(request):
    query = request.GET.get("query")
    products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, "search.html", {
        "query": query,
        "products": products,
    })
