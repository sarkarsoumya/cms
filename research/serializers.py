from rest_framework import serializers
from .models import Resource, ResourceType

from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
            

class ResourceTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ResourceType
        fields = ('id', 'name')


class ResourceSerializer(serializers.ModelSerializer):
    resource_type = ResourceTypeSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Resource
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')