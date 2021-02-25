from django.contrib.auth.models import User
from .models import Menu, Dish
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'name', 'description', 'price', 'preparation_time', 'add_date', 'update_date', 'is_vege']


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    dishes = DishSerializer(many=True)

    class Meta:
        model = Menu
        fields = ['id', 'menu_name', 'description', 'add_date', 'update_date', 'dishes']
