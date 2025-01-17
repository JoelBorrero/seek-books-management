import json

from apps.book.models import Book


books = json.load(open('./setup/db_population.json'))

for book in books:
    Book.objects.create(book)
