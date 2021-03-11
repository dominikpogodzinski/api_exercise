from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Dish, Menu


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"required": True, "write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ["id", "name", "description", "price", "preparation_time", "added_on", "update_on", "is_vege"]


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "title", "description", "added_on", "update_on", "dishes"]
