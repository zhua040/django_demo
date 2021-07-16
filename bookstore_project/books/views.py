from typing import ContextManager
from django.shortcuts import render
import json

# booksData = open("/Users/chaof/Desktop/Django_Project_Demo/bookstore_project/books.json").read()
booksData = open('C:/Users/chaof/Desktop/Django_Project_Demo/bookstore_project/books.json').read()
data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)


def show(request, id):
    singleBook = list()

    for book in data:
        if book['id'] == id:
            singleBook = book

    context = {'book': singleBook}
    return render(request, 'books/show.html', context)