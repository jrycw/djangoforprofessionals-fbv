from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("<uuid:pk>/", views.book_detail, name="book_detail"),
    path("search/", views.search_list, name="search_results"),
]
