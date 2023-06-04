from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category, OrderItem
from .cart import Cart
from .forms import OrderCreateForm


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


@login_required
def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart_detail.html", {"cart": cart})


@login_required
def payment(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            total_price = 0
            for item in cart:
                product = item["product"]
                total_price += product.price * item["quantity"]

            order = form.save(commit=False)
            order.shopped_by = request.user
            order.paid_amount = total_price
            order.save()

            for item in cart:
                product = item["product"]
                quantity = item["quantity"]
                price = product.price * quantity
                item = OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

            cart.clear()

            return redirect("payment_successful")
    else:
        form = OrderCreateForm()

    return render(request, "payment.html", {
        "cart": cart,
        "form": form
    })


@login_required
def order_history(request):
    orders_items = OrderItem.objects.filter(order__shopped_by=request.user)
    return render(request, "order_history.html", {
        "orders_items": orders_items
    })


def payment_successful(request):
    return render(request, "payment_successful.html")
