from rest_framework import serializers
from .models import Event, Attendancing


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttendancingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendancing
        fields = '__all__'  