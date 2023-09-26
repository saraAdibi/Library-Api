from django.shortcuts import render
from rest_framework import generics
from .models import Library
from .serializer import UserSerializer, LibrarySerializer
from django.contrib.auth import get_user_model

# Create your views here.
user = get_user_model()


class LibraryCreateApiView(generics.ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibraryApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class UserApiView(generics.ListAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer
