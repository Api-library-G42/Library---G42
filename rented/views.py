from rest_framework import generics
from .models import Rented
from .serializers import RentedSerializer

from .permissions import EnsureExistPermissions, AuthPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class RentedView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthPermissions]

    queryset = Rented.objects.all()
    serializer_class = RentedSerializer


class RentedDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AuthPermissions]

    queryset = Rented.objects.all()
    serializer_class = RentedSerializer
