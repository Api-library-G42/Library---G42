from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsUserOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
