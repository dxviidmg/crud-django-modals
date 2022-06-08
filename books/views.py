from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from django.urls import reverse_lazy
from .forms import BookModelForm
from bootstrap_modal_forms.generic import BSModalCreateView


class BookListView(ListView):
    model = Book



class BookCreateView(BSModalCreateView):
    template_name = 'books/create_book.html'
    form_class = BookModelForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('list_book')