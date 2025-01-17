from django.db import models

from project.db import BaseModel, ModelMetaclass


class Book(BaseModel):
    class Genre(models.TextChoices):
        ADVENTURE = "a", "Adventure"
        FANTASY = "f", "Fantasy"
        HORROR = "h", "Horror"
        ROMANCE = "r", "Romance"
        SCIENCE_FICTION = "sf", "Science Fiction"

    title: str
    author: str
    published_year: int
    genre: Genre
    price: float
    pages: int = None  # Optional field

    _meta = ModelMetaclass(collection_name="books")
