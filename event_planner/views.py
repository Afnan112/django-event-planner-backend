from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response

# Create your views here.
class EventListView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=200)