from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.urls import reverse

from homepage.utils import find_random_integer

user_model = get_user_model()


def homepage(request):
    if request.user.is_authenticated:
        print(request.user)
        print(type(request.user))
    else:
        template_name = "users/login.html"
        return render(
            request,
            template_name,
        )
    context = {
        "rand_int": find_random_integer(),
    }
    template_name = "homepage/homepage.html"
    return render(
        request,
        template_name,
        context,
    )


def user_logout(request):
    logout(request)
    return redirect(
        reverse("homepage:homepage"),
    )
