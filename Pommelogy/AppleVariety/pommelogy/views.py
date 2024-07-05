from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, viewsets
from .serializers import MyTokenObtainPairSerializer, UserSerializer, AppleVarietySerializer
from django.contrib.auth.models import User
from .models import AppleVariety, CustomUser

class AppleVarietyViewSet(viewsets.ModelViewSet):
    queryset = AppleVariety.objects.all()
    serializer_class = AppleVarietySerializer

class MyObtainTokenPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()

class AppleVarietyViewSet(viewsets.ModelViewSet):
    queryset = AppleVariety.objects.all()
    serializer_class = AppleVarietySerializer