from django.urls import path
from .views import EventListCreateView, EventDetailView, CreateAttendanceAPI

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # api/all-event/int:event_id/
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_id>/add-attendance/', CreateAttendanceAPI.as_view(), name='add_attendance'),
    # path('events/<int:event_id>/add-note/', NoteCreateView.as_view(), name='add-note'),
    # path('events/<int:event_id>/notes/', NoteDetailView.as_view(), name='event-notes')


]