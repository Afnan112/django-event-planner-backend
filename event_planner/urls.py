from django.urls import path
from .views import EventListCreateView, EventDetailView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    # api/all-event/int:event_id/
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail')
]