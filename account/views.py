from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .serializers import SignUpSerializer, ProfileSerializer
from .models import UserProfile, User
from .permissions import IsOwnerOrReadOnly
# Create your views here.


class SignUp(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer

class ProfileView(ModelViewSet):
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsOwnerOrReadOnly()]
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)