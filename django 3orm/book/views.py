from django.shortcuts import render
from .models import Book, Author, Comments


def home(request):
    return render(request, 'home.html')

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})



def authors(request):
    authors = Author.object.all()
    return render(request, 'authors.html', {'authors': authors})


def comments(request):
    comments = Comments.objects.all()
    return render(request, 'comments.html', {'comments': comments})



