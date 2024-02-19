from django.urls import path

from apps.books.views import BookListView, BookDetailView, AuthorDetailView, GenreDetailView

app_name = "books"

urlpatterns = [
    path('', BookListView.as_view(), name="book-list"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book-detail"),
    path('author/<int:pk>', AuthorDetailView.as_view(), name="author-detail"),
    path('genre/<int:pk>', GenreDetailView.as_view(), name="genre-detail"),
    # path('<pk>/', GenreView.as_view(), name="book-detail"),
]
