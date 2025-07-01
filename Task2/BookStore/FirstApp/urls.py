from django.urls import path
from .views import (AuthorListCreateAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,GenreListCreateAPIView,GenreRetrieveUpdateDestroyAPIView,)

urlpatterns=[
    path('authors/',AuthorListCreateAPIView.as_view(),name='author-list-create'),
    path('books/',BookListCreateAPIView.as_view(),name='book-list-create'),
    path('genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
     path('genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(),name='book-detail'),
]