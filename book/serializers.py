from rest_framework import serializers
from .models import Book
from copies.models import Copies
from django.core.mail import send_mail
from django.conf import settings


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
            list = []

            for users in obj.favorites.all():
                list.append(users.email)
            send_mail(
                subject="Livro favoritado",
                message=f"Olá o livro {obj.title} está disponível para locação",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=list,
                fail_silently=False,
            )
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
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "favorites"]
        read_only_fields = ["id", "favorites"]
        depth = 1

    def get_favorites(self, instance):
        list = []
        for users in instance.favorites.all():
            list.append(users.email)

        return list

    def update(self, instance, validated_data):
        instance.favorites.add(validated_data.get("favorites"))
        instance.save()

        return instance
