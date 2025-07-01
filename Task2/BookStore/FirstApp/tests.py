from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author, Book, Genre
from .serializers import BookSerializer
from datetime import date

class BookSerializerTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            name="Test Author",
            bio="Bio of the author",
            date_of_birth="1990-01-01"
        )
        self.genre = Genre.objects.create(name="Fiction")

    def test_valid_book_serializer(self):
        data = {
            "title": "Valid Book",
            "author_id": self.author.id,
            "published_date": "2023-01-01",
            "genre_ids": [self.genre.id]
        }
        serializer = BookSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_short_title(self):
        data = {
            "title": "No",
            "author_id": self.author.id,
            "published_date": "2023-01-01",
            "genre_ids": [self.genre.id]
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("title", serializer.errors)

    def test_invalid_future_date(self):
        future_date = date.today().replace(year=date.today().year + 1)
        data = {
            "title": "Future Book",
            "author_id": self.author.id,
            "published_date": future_date,
            "genre_ids": [self.genre.id]
        }
        serializer = BookSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("non_field_errors", serializer.errors)


class BookViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(
            name="Author A",
            bio="Test bio",
            date_of_birth="1980-01-01"
        )
        self.genre = Genre.objects.create(name="Sci-Fi")

    def test_create_book(self):
        data = {
            "title": "New Book",
            "author_id": self.author.id,
            "published_date": "2023-05-01",
            "genre_ids": [self.genre.id]
        }
        response = self.client.post("/api/books/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_get_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

