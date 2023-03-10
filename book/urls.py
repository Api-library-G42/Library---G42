from django.urls import path
from .views import BookView, BookDetailView, FavoritesBookView

urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<uuid:pk>/", BookDetailView.as_view()),
    path("books/<uuid:pk>/favorites/", FavoritesBookView.as_view()),    
]
