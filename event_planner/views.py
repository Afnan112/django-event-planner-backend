from django.shortcuts import render
from rest_framework.views import APIView
from .models import Event, Attendancing, Notes
from .serializers import EventSerializer, AttendancingSerializer, NotesSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.exceptions import NotFound

# Create your views here.
class EventListCreateView(APIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    # Looking for the event in the DB using PK
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)

    # Get event's details using PK
    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=200)
    
    # Delet event using PK
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
    
# Ref => cat-collector exists(), filter()
# https://medium.com/@altafkhan_24475/post-method-of-apiview-in-django-rest-framework-2aa361c4d6e0
class CreateAttendanceAPI(APIView):
    # Add a user's attendance to a specific event
    def post(self, request, event_id):

        # Here check for event
        event = get_object_or_404(Event, pk=event_id)
        #get user id from url
        user = request.user

        if Attendancing.objects.filter(event=event, user_id=user.id).exists(): 
                return Response({'message': 'User is already registered for this event'}, status=400)
            
        data = request.data.copy()
        data['event'] = event.id
        data['user'] = user.id 

        serializer = AttendancingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    # Return all events attended by the current user
    def get (self, request):
        events = Attendancing.objects.filter(user_id=request.user)
        serializer = AttendancingSerializer(events, many=True)
        return Response(serializer.data, status=200)


class CancelAttendanceAPI(APIView):
        # Ref
        # https://stackoverflow.com/questions/40758860/how-to-return-all-records-but-exclude-the-last-item
        # https://docs.djangoproject.com/en/5.2/ref/models/querysets/#exclude
        def delete (self, request, event_id):
            attendances = Attendancing.objects.filter(event_id=event_id, user_id=request.user.id)

            if attendances.exists():
                attendances.delete()  
                return Response(status=204)
            else:
                return Response({"error": "Attendance not found"}, status=404)
            
#  Create a new note associated with a specific event
class NoteCreateView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)
    
    def post(self, request, event_id):
        event = self.get_object(event_id)

        data = request.data.copy()
        data['event'] = event.id
        serializer = NotesSerializer(data=data)
        if serializer.is_valid():
            serializer.save(event=event)
            return Response(serializer.data, status=201)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Get all notes related to the event 
    
class NoteDetailView(APIView):
    def get(self, request, event_id):
        notes = Notes.objects.filter(event_id = event_id)
        if not notes:
            raise NotFound("No notes found for this event")
        
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=200)


class SignUpView(APIView):
    permission_classes = [AllowAny]
    # When we recieve a POST request with username, email, and password. Create a new user.
    def post(self, request):
        print('data', request.data)
        # Using .get will not error if there's no username
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            validate_password(password)
        except ValidationError as err:
            return Response({'error': err.messages}, status=400)

        # Actually create the user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # create an access and refresh token for the user and send this in a response
        tokens = RefreshToken.for_user(user)
        return Response(
            {
                'refresh': str(tokens),
                'access': str(tokens.access_token)
            },
            status=201
        )