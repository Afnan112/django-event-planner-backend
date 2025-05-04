from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event (models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Attendancing (models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Attendance for: {self.event.title}'
    

class Notes(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='notes')

    def str(self):
        return f'Note for: {self.event.title}'
