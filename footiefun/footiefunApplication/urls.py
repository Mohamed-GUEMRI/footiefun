from django.urls import path,include
from rest_framework import routers
from views import ReservationViewSet,MatchViewSet,TouroitViewSet,StadeViewSet,UserViewSet

router = routers.DefaultRouter()
router.register(r'reservations', ReservationViewSet)
router.register(r'matches', MatchViewSet)
router.register(r'tournoits', TouroitViewSet)  # Note the spelling correction here
router.register(r'stades', StadeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]