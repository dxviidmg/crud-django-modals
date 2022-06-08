from django.urls import path
from books.views import BookListView, BookCreateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='list_book'),
    path('create/', BookCreateView.as_view(), name='create_book'),
]