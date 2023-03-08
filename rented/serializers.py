from rest_framework import serializers
from datetime import datetime, timedelta

from .models import Rented


class RentedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rented
        fields = ["id", "rented_at", "devolution_at", "book_time", "copy", "user"]
        read_only_fields = [
            "rented_at",
            "devolution_at",
            "book_time",
        ]

    def get_book_time(self, obj):
        data_atual = datetime.now()
        data_futura = data_atual + timedelta(days=14)

        return data_futura
