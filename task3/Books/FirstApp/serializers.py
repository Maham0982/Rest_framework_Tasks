from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    internal_notes = serializers.CharField(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        user = self.context['request'].user
        if not user.is_staff:
            data.pop('internal_notes', None)
        return data


class BookDetailSerializer(serializers.ModelSerializer):
    days_since_published = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'published_date', 'days_since_published']

    def get_days_since_published(self, obj):
        if obj.published_date:
            return (date.today() - obj.published_date).days
        return None


class BookReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'published_date'] 

        