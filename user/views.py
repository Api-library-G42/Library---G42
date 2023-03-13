from .models import User
from .serializers import RequestUserSerializer, UserSerializer, CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsColaboratorHasPermission, IsUserOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from drf_spectacular.utils import extend_schema


class UserView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsColaboratorHasPermission]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(request=RequestUserSerializer)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginJWTView(TokenObtainPairView):
    @extend_schema(response={"token": str})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    serializer_class = CustomJWTSerializer
