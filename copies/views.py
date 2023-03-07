from .models import Copies
from rest_framework import generics
from .serializers import CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsColaborator


class CopyView(generics.ListAPIView):
    queryset = Copies.objects.all()
    serializer_class = CopySerializer


class CopyDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaborator]
    queryset = Copies.objects.all()
    serializer_class = CopySerializer
