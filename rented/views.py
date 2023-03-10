from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RentedSerializer
from .permissions import AuthPermissions
from rest_framework import generics
from .models import Rented


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
