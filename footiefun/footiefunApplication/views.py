from django.shortcuts import render
from rest_framework import viewsets
from .models import Stade
from .serializers import StadeSerializer


class StadeViewSet(viewsets.ModelViewSet):
    queryset = Stade.objects.all()
    serializer_class= StadeSerializer

# Create your views here.
