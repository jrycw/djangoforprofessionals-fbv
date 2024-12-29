from django.urls import path
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about/", views.about_page, name="about"),
]
