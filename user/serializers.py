from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User
from rented.models import Rented


class loginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, read_only=True)


class RequestUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "password",
            "username",
            "age",
            "is_colaborator",
        ]


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
            "blocked_at",
            "historic_copies_rented",
        ]
        read_only_fields = ["is_superuser", "historic_books"]
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

    historic_copies_rented = serializers.SerializerMethodField()

    def get_historic_copies_rented(self, obj) -> list:
        user_id = str(obj.id)
        historic_books = Rented.objects.filter(user_id=user_id)

        list = []
        for books in historic_books.all():
            list.append(books.copy_id)

        return list

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
        token = super().get_token(user)
        token["blocked"] = user.blocked

        return token
