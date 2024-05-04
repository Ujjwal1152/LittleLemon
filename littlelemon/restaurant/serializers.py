from rest_framework import serializers
from .models import Menu,booking

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
        
class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
        
        
        