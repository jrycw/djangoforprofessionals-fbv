from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .forms import CustomUserCreationForm


def signup(request: HttpRequest):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("pages:home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
    else:
        form = CustomUserCreationForm()

        context = {"form": form}
        return render(request, "registration/signup.html", context)
