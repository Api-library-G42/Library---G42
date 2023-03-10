from book.permissions import IsColaboratorOrReadOnly
from .models import Book
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, FavoritesBookSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from book.serializers import FavoritesBookSerializer
from rest_framework.permissions import IsAuthenticated


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaboratorOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class FavoritesBookView(generics.RetrieveAPIView, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = FavoritesBookSerializer

    def perform_update(self, serializer):
        return serializer.save(favorites=self.request.user)
