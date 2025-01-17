# This views file uses the pure MongoDB driver to interact with the database.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(["GET", "POST"])
def book_list(request: Request) -> Response:
    """
    Get a list of books or create a new book.
    """
    serializer_class = BookSerializer

    if request.method == "GET":
        books = Book.objects.all()
        pagination_class = PageNumberPagination()
        page = pagination_class.paginate_queryset(books, request)
        paginated_response = pagination_class.get_paginated_response(page)
        return Response(paginated_response.data)

    elif request.method == "POST":
        data = request.data
        serializer = serializer_class(data=data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(["GET", "DELETE", "PUT"])
def book_detail(request: Request, id: str) -> Response:
    """
    Get, delete, or update a book by its ID.
    """
    if request.method == "GET":
        book = Book.objects.get(id=id)
        if book:
            return Response(BookSerializer(book).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "DELETE":
        book = Book.objects.get(id=id)
        if book:
            success = book.delete()
            if success:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == "PUT":
        book = Book.objects.get(id=id)
        if book:
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                book = serializer.save(id=book._id)
                return Response(BookSerializer(book).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(["GET"])
def book_average_price(request: Request, year: int) -> Response:
    """
    Get the average price of books published in a given year.

    Args:
        year: The year to get the average price for.

    Returns:
        A dictionary with the year, count of books, and average price for the given year.
    """
    response = {"year": year, "count": 0, "average_price": 0}

    pipeline = [
        {"$match": {"published_year": int(year)}},
        {"$group": {"_id": "$published_year", "average_price": {"$avg": "$price"}, "count": {"$count": {}}}},
    ]

    aggregate_data = Book.objects.aggregate(pipeline).data

    if aggregate_data:
        data = aggregate_data[0]
        response["average_price"] = data["average_price"]
        response["count"] = data["count"]

    return Response(response, status=status.HTTP_200_OK)
