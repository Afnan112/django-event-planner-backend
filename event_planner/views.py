from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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


class EventDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)

    def get(self, request, pk):
        # Get the post object
        # Serialize it with the PostSerializer
        # Return it
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=200)
    
    def delete(self, request, pk):
        # Get the post
        # Delete the post
        # Send an appropriate response
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)