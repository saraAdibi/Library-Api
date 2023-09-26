from .models import Library
from rest_framework import serializers
from django.contrib.auth import get_user_model

user = get_user_model()


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    library = LibrarySerializer(read_only=True, many=True)

    class Meta:
        model = user
        fields = '__all__'
