from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# router.register(r"users", UserViewSet, basename="users")

urlpatterns = []

urlpatterns += router.urls
