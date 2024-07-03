from django.urls import path
from .views import home, books, authors

urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
    path('authors/', authors, name='authors'),
]