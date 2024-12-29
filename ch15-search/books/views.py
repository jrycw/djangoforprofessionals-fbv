from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.db.models import Q
from .models import Book


@login_required
def book_list(request: HttpRequest):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/book_list.html", context)


@login_required
@permission_required("books.special_status", raise_exception=True)
def book_detail(request: HttpRequest, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {"book": book}
    return render(request, "books/book_detail.html", context)


def search_list(request: HttpRequest):
    query = request.GET.get("q", None)
    if query is None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
    context = {"books": books}
    return render(request, "books/search_results.html", context)
