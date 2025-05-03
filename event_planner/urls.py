from django.urls import path
from .views import EventListCreateView, EventDetailView, CreateAttendanceAPI

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # api/all-event/int:event_id/
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('events/<int:event_id>/add-attendance/', CreateAttendanceAPI.as_view(), name='api_add_attendance'),
]