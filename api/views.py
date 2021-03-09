from django.contrib.auth.models import User
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from .models import Dish, Menu
from .serializers import DishSerializer, MenuSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.annotate(dish=Count("dishes")).filter(dish__gt=1)
    serializer_class = MenuSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    filter_backends = (
        DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filter_fields = ("name", "add_date", "update_date")
    ordering_fields = ("name",)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
