from django.db import models

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