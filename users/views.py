from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "authenticate/register.html", context)
