from django.urls import path,include
from rest_framework import routers
from .views import StadeViewSet

routre=routers.DefaultRouter()
routre.register('Stade',StadeViewSet)

urlpatterns=[
    path('',include(routre.urls))
]