from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu')
router.register(r'dish', views.DishViewSet, basename='dish')

schema_view = get_swagger_view(title='api_swagger')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('api-token-auth/', obtain_auth_token),
    url(r'^', include(router.urls)),
]
