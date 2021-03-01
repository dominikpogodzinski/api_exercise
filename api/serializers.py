from django.contrib.auth.models import User
from .models import Menu, Dish
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'preparation_time', 'add_date', 'update_date', 'is_vege']


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'description', 'add_date', 'update_date', 'dishes']
