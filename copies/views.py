from .models import Copies
from rest_framework import generics
from .serializers import CopySerializer


class CopyView(generics.ListAPIView):
    queryset = Copies.objects.all()
    serializer_class = CopySerializer
