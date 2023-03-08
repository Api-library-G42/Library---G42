from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from datetime import datetime
import pytz


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "is_superuser",
            "password",
            "username",
            "age",
            "blocked",
            "is_colaborator",
            "blocked_at"
        ]
        read_only_fields = ["is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )

    def create(self, validated_data):
        if validated_data["is_colaborator"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        tz = pytz.timezone("America/Sao_Paulo")
        current_date = datetime.now(tz)
        if user.blocked:
            if user.blocked_at < current_date:
                user_updated = UserSerializer(user, data={"blocked": False, "blocked_at": None}, partial=True)
                user_updated.is_valid()

                user_updated.save()

        token = super().get_token(user)
        token["blocked"] = user.blocked

        return token
