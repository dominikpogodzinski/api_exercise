from django.shortcuts import get_object_or_404

from .models import Menu, Dish
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import MenuSerializer, DishSerializer, UserSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )
    filter_backends = (filters.OrderingFilter, )
    ordering_fields = ('name', )

    # @property
    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        add_date = self.request.query_params.get('add_date', None)
        update_date = self.request.query_params.get('update_date', None)

        if name:
            menu = Menu.objects.filter(name__icontains=name)
        else:
            if add_date or update_date:
                menu = Menu.objects.filter(add_date=add_date, update_date=update_date)
            else:
                menu = Menu.objects.all()
        return menu

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        serializer = MenuSerializer(queryset, many=True)
        return Response(serializer.data)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
