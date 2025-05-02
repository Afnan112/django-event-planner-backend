from django.urls import path
from .views import EventListCreateView, EventDetailView, add_attendance

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # api/all-event/int:event_id/
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('attendance/<int:event_id>/add-attendance/', add_attendance, name='add_attendance'),

]