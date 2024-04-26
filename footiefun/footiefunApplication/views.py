from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Reservation,Match,Tournoit, Stade
from .serializers import ReservationSerializer,MatchSerializer,TournoitSerializer,StadeSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class TouroitViewSet(viewsets.ModelViewSet):
    queryset = Tournoit.objects.all()
    serializer_class = TournoitSerializer

class StadeViewSet(viewsets.ModelViewSet):
    queryset = Stade.objects.all()
    serializer_class= StadeSerializer
