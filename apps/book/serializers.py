from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.Serializer):
    _id = serializers.UUIDField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    published_year = serializers.IntegerField()
    price = serializers.FloatField()
    pages = serializers.IntegerField(required=False)
    genre = serializers.ChoiceField(choices=Book.Genre.choices)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    genre_display = serializers.SerializerMethodField()

    def save(self, **kwargs):
        book = Book(**self.validated_data)
        if kwargs.get("id"):
            book._id = kwargs.get("id")
        book.save()
        return book

    def get_genre_display(self, obj):
        return Book.Genre(obj.genre).label
