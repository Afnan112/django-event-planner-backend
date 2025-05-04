from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event, Attendancing
from .serializers import EventSerializer, AttendancingSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from rest_framework import status
# from rest_framework.exceptions import NotFound

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
        # Get the event
        # Delete the event
        # Send an appropriate response
        event = self.get_object(pk)
        event.delete()
        return Response(status=204)
    
    def patch(self, request, pk):
        # get the event to update
        # If the update is valid save it
        # return an approprate response
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

class CreateAttendanceAPI(APIView):
    def post(self, request, event_id):

        event = get_object_or_404(Event, pk=event_id)
        print(event)

        data = request.data.copy()
        data['event'] = event.id

        serializer = AttendancingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def add_attendance_to_event(request, event_id, atten_id):
        try:
            event = Event.objects.get(pk=event_id)
            attendance = Attendancing.objects.get(pk=atten_id)

            event.event.add (attendance)
            return Response({'message': 'Event to was Added!'}, status=200)
        except Event.DoesNotExist:
            return Response({'error': 'The Event Does Not Exist'}, status=404)
        except Attendancing.DoesNotExist:
            return Response({'error': 'The Attendance Does Not Exist'}, status=404)
        except:
            return Response({'error': 'Something went wrong'}, status=500)



# class NoteCreateView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Event, pk=pk)
    
#     def post(self, request, event_id):
#         event = self.get_object(event_id)

#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(event=event)
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

    
# class NoteDetailView(APIView):
#     def get(self, request, event_id):
#         notes = Noting.objects.filter(event_id = event_id)
#         if not notes:
#             raise NotFound("No notes found for this event")
        
#         serializer = NoteSerializer(notes, many=True)
#         return Response(serializer.data, status=200)