from django.urls import path
from .views import RentedView

urlpatterns = [
    path("rented/", RentedView.as_view()),
]
