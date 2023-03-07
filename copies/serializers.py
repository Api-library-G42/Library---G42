from rest_framework import serializers
from .models import Copies


class CopySerializer(serializers.ModelSerializer):
    # book = serializers.SerializerMethodField()
    book = serializers.CharField(source="book.title", read_only=True)

    class Meta:
        model = Copies
        fields = ["id", "is_available", "book"]
        depth = 0
