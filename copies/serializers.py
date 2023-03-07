from rest_framework import serializers
from .models import Copies


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copies
        fields = ["id", "is_available", "book"]
        depth = 2
