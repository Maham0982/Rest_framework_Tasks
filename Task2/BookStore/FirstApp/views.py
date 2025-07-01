from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book, Author,Genre
from rest_framework import generics
from .serializers import BookSerializer,AuthorSerializer,GenreSerializer

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data
        print("Data: ", data)
        author_obj = Author.objects.get(id=data.get('author_id'))
        Book.object.create(
            title=data.get('title'),
            author=author_obj,
            published_date=data.obj('published_date')
        )
        return Response({"message": "Book record created successfully"}, status=200)

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

    def get_serializer_context(self):
        return {'request': self.request}



class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class GenreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class =GenreSerializer

    def get_serializer_context(self):
        return {'request': self.request}
    

class GenreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_serializer_context(self):
        return {'request': self.request}



