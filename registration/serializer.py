from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        # fields = ('id','fullname') OR for all columns in the moddel use below
        fields = '__all__'