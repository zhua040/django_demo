from typing import ContextManager
from django.shortcuts import render
import json

# booksData = open("/Users/chaof/Desktop/Django_Project_Demo/bookstore_project/books.json").read()
booksData = open('C:/Users/chaof/Desktop/Django_Project_Demo/bookstore_project/books.json').read()
data = json.loads(booksData)


def index(request):
    context = {'books': data}
    return render(request, 'books/index.html', context)