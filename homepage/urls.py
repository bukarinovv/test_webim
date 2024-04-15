from django.urls import path

import homepage.views as views

app_name = "homepage"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('logout', views.user_logout, name='logout'),
]
