import django_filters
from .models import Book
from rest_framework.filters import BaseFilterBackend

class BookFilter(django_filters.FilterSet):
    published_after = django_filters.DateFilter(field_name='published_date', lookup_expr='gte')
    published_before = django_filters.DateFilter(field_name='published_date', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'published_after', 'published_before']


class CustomBookFilterBackend(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        start_letter = request.query_params.get('starts_with')
        if start_letter:
            queryset = queryset.filter(title__istartswith=start_letter)

        year = request.query_params.get('published_year')
        if year:
            queryset = queryset.filter(published_date__year=year)

        return queryset