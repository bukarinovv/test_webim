from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("oauth/", include("social_django.urls", namespace="social")),
    path("", include("homepage.urls")),
    path(
        "accounts/profile/",
        RedirectView.as_view(url="/"),
        name="profile_redirect",
    ),
]
