from rest_framework import serializers
from .models import Reservation,Match,Tournoit
class ReservationSerializer (serializers.ModelSerializer):

    class Meta :
        model =Reservation
        fields ='__all__'
       # fields =['id','model','type']


class MatchSerializer (serializers.ModelSerializer):

    class Meta :
        model =Match
        fields ='__all__'
     
       
class TournoitSerializer (serializers.ModelSerializer):

    class Meta :
        model =Tournoit
        fields ='__all__'
     