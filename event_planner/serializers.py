from rest_framework import serializers
from .models import Event, Attendance, Note

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        # fields = '__all__'  
        fields = ['user_id', 'event_id'] 


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # fields = '__all__'  
        fields = ['user_id', 'event_id', 'content'] 