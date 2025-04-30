from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response

# Create your views here.
class EventListCreateView(APIView):
    # This function to dispaly all events exist DB
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=200)
    
    # This function to ctrate a new event in DB
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)