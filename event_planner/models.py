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
    

class Attendance (models.Model):
    # Link with user
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} - {self.event_id.title}'
    

class Note (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f'{self.user_id} - {self.event_id.title} - {self.content}'