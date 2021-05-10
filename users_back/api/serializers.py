from rest_framework import serializers
from .models import Api

class ApiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Api
        fields = ('pk', 'first_name', 'last_name', 'email', 'created_at')