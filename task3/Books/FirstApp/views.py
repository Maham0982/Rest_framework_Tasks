from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from .filters import BookFilter
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer, BoookWriteSerializer
from .pagination import CustomPagination ,BookCursorPagination
from datetime import date

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filterset_class=BookFilter
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    search_fields=['title']
    ordering_fields=['published_date','title']
    serializer_class=BookSerializer
    #pagination_class=CustomPagination 
    pagination_class=BookCursorPagination
    filterset_class=BookFilter  

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return BookWriteSerializer
        if self.request.query_params.get('verbose') == 'true':
            return BookDetailSerializer
        if self.action == 'retrieve':
            return BookDetailSerializer 
        return BookSerializer

    @action(detail=True, methods=['get'])
    def statistics(self, request, pk=None):
        book = self.get_object()
        stats = {
            "title": book.title,
            "published_year": book.published_date.year,
            "days_since_published": (date.today() - book.published_date).days
        }
        return Response(stats)

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_books = Book.objects.filter(title__icontains="featured")
        page = self.paginate_queryset(featured_books)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(featured_books, many=True)
        return Response(serializer.data)

