from django.urls import path
from .views import EventListCreateView, EventDetailView, CreateAttendanceAPI, CancelAttendanceAPI,NoteCreateView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # api/all-event/int:event_id/
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    # Resister a user for an evnt
    path('events/<int:event_id>/add-attendance/', CreateAttendanceAPI.as_view(), name='add_attendance'),
    # views user's registered events 
    path('attendance/my_events', CreateAttendanceAPI.as_view(), name='my_attendance'),
    # Cancel user attendance for an event
    path('attendance/<int:event_id>/cancel/', CancelAttendanceAPI.as_view(), name="cancel_attendance" ),
    path('events/<int:event_id>/add-note/', NoteCreateView.as_view(), name='add-note'),
    # path('events/<int:event_id>/notes/', NoteDetailView.as_view(), name='event-notes')


]