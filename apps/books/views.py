from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.books.models import Book, BookAuthor, BookGenre


class BookListView(ListView):
    model = Book
    template_name = "books/book-list.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    model = Book
    slug_url_kwarg = 'slug'
    template_name = "books/book-detail.html"
    context_object_name = "book"

class GenreDetailView(DetailView):
    model = BookGenre
    template_name = "books/genre-detail.html"
    context_object_name = "genre"


class AuthorDetailView(DetailView):
    model = BookAuthor
    template_name = "books/author-detail.html"
    context_object_name = "author"

