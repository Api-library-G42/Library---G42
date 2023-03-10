from django.urls import path
from .views import CopyView, CopyDetailView

urlpatterns = [
    path("copies/", CopyView.as_view()),
    path("copies/<uuid:pk>/", CopyDetailView.as_view()),
]
