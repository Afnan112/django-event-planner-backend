from rest_framework import serializers
from .models import Event, Attendancing, Notes


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttendancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendancing
        fields = '__all__'  


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'  
