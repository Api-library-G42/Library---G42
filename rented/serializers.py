from rest_framework import serializers
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta
from .models import Rented
from user.models import User
from user.serializers import UserSerializer
from copies.models import Copies
from copies.serializers import CopySerializer
import pytz


class RentedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rented
        fields = ["id", "rented_at", "devolution_at", "book_time", "copy", "user"]
        read_only_fields = ["rented_at", "devolution_at", "book_time"]

    def create(self, validated_data):
        tz = pytz.timezone("America/Sao_Paulo")
        current_date = datetime.now(tz)
        user = get_object_or_404(User, id=validated_data["user"].id)
        copy = get_object_or_404(Copies, id=validated_data["copy"].id)

        if copy.is_available == False:
            raise serializers.ValidationError(
                detail={"error": "Está copia não esta disponivel"}, code=404
            )

        if user.blocked:
            if user.blocked_at < current_date:
                user_updated = UserSerializer(
                    user, data={"blocked": False, "blocked_at": None}, partial=True
                )
                user_updated.is_valid()

                user_updated.save()
            else:
                raise serializers.ValidationError(
                    detail={"error": "Usuario bloqueado"}, code=404
                )

        data_atual = datetime.now()
        data_futura = data_atual + timedelta(days=14)

        validated_data["book_time"] = data_futura

        copy_updated = CopySerializer(copy, data={"is_available": False}, partial=True)
        copy_updated.is_valid()
        copy_updated.save()

        return Rented.objects.create(**validated_data)

    def update(self, instance: Rented, validated_data: dict) -> Rented:
        data_atual = datetime.now()
        data_futura = data_atual + timedelta(days=7)

        tz = pytz.timezone("America/Sao_Paulo")

        rented = get_object_or_404(Rented, id=instance.id)

        if rented.devolution_at is not None:
            raise serializers.ValidationError(
                detail={"error": "Este livro já foi entregue"}, code=404
            )

        instance.devolution_at = datetime.now(tz)

        if instance.devolution_at > instance.book_time:
            user = get_object_or_404(User, id=instance.user.id)

            user_updated = UserSerializer(
                user, data={"blocked": True, "blocked_at": data_futura}, partial=True
            )
            user_updated.is_valid()

            user_updated.save()

        copy = get_object_or_404(Copies, id=instance.copy.id)

        copy_updated = CopySerializer(copy, data={"is_available": True}, partial=True)
        copy_updated.is_valid()
        copy_updated.save()

        instance.save()

        return instance
