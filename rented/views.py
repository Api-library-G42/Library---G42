from rest_framework import generics
from .models import Rented
from .serializers import RentedSerializer


class RentedView(generics.ListCreateAPIView):

    queryset = Rented.objects.all()
    serializer_class = RentedSerializer
