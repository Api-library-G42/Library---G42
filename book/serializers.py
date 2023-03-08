from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Book
from copies.models import Copies
from copies.serializers import CopySerializer
from user.serializers import UserSerializer


class BookSerializer(serializers.ModelSerializer):
    copies = serializers.SerializerMethodField()
    available = serializers.SerializerMethodField()
    copies_qts = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "available",
            "created_at",
            "updated_at",
            "copies_qts",
            "copies",
        ]

    def get_copies(self, obj):
        return len(obj.copies.values())

    def get_available(self, obj):
        if len(obj.copies.filter(is_available=True)) > 0:
            return True
        else:
            return False

    def create(self, validated_data):
        copies_qts_loop = validated_data.pop("copies_qts")
        book = Book.objects.create(**validated_data)

        copies_instances = [Copies(book=book) for _ in range(copies_qts_loop)]

        Copies.objects.bulk_create(copies_instances)

        return book


class FavoritesBookSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # book_id = BookSerializer(read_only=True)
    # user_id = UserSerializer(read_only=True, many=True)
    class Meta:
        model = Book
        fields = ["id", "favorites"]
        read_only_fields = ["id", "favorites"]

    def update(self, instance, validated_data):
        instance.favorites.add(validated_data.get("favorites"))
        instance.save()
        
        return instance
        