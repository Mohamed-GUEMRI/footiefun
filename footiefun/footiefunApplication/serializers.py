from rest_framework import serializers
from .models import Reservation,Match,Tournoit, Stade,User

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

class StadeSerializer(serializers.ModelSerializer):
    class Meta : 
        model=Stade
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'