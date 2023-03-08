from django.urls import path
from .views import RentedView, RentedDetailView

urlpatterns = [
    path("rented/", RentedView.as_view()),
    path("rented/<uuid:pk>/", RentedDetailView.as_view()),
]
