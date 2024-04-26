from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Reservation,Match,Tournoit # Assuming you have a Reservation model
from .serializers import ReservationSerializer,MatchSerializer,TournoitSerializer  # Assuming you have a serializer for the Reservation model


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer



class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer



class TouroitViewSet(viewsets.ModelViewSet):
    queryset = Tournoit.objects.all()
    serializer_class = TournoitSerializer













