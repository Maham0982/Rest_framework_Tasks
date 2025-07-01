from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import CursorPagination

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookCursorPagination(CursorPagination):
    page_size = 3
    ordering = '-published_date' 