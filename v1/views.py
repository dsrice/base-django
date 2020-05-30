from django.shortcuts import render
from rest_framework import viewsets, filters

from .models import User
from .serializers.users import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer