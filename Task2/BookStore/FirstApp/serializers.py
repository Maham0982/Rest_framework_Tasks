from rest_framework import serializers
from .models import Book, Author,Genre
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Genre
        fields=['url','id','name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer(read_only=True)
    genres=serializers.StringRelatedField(many=True, read_only=True)
    genre_ids=serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(),many=True,write_only=True)
    days_since_published = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [ 'url', 'title', 'author', 'published_date','genres','genre_ids', 'days_since_published']
        depth = 1  

    def get_days_since_published(self, obj):
        return (date.today() - obj.published_date).days

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value

    def validate(self, data):
        if data['published_date'] > date.today():
            raise serializers.ValidationError("Publication date cannot be in the future.")
        return data


    def create(self, validated_data):
        genre_ids=validated_data.pop('genre_ids',[])
        book=Book.objects.create(**validated_data)
        book.genres.set(genre_ids)
        return book
    
    def update(self, instance, validated_data):
        genre_ids=validated_data.pop('genre_ids',None)
        if genre_ids is not None:
            instance.genres.set(genre_ids)
        return super().update(instance,validated_data)    
    

