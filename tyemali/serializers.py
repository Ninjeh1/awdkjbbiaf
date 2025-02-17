from rest_framework import serializers
from .models import  Penali


class PenaliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penali
        fields = '__all__'
        read_only_fields = ['player']
