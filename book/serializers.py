from rest_framework import serializers
from .models import Book
from copies.models import Copies
from copies.serializers import CopySerializer


class BookSerializer(serializers.ModelSerializer):
    copies = CopySerializer(many=True, read_only=True)
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

    def create(self, validated_data):
        copies_qts_loop = validated_data.pop("copies_qts")
        book = Book.objects.create(**validated_data)

        copies_instances = [Copies(book=book) for _ in range(copies_qts_loop)]

        Copies.objects.bulk_create(copies_instances)

        return book
