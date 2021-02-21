from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'dish', views.DishViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
