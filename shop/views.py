from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category
from .cart import Cart


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


@login_required
def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect("cart_detail")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(str(product_id))

    return redirect("cart_detail")


def change_quantity(request, product_id):
    action = request.GET.get("action", "")
    if action:
        quantity = 1
        if action == "decrease":
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity=quantity, update_quantity=True)

    return redirect("cart_detail")


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart_detail.html", {"cart": cart})
