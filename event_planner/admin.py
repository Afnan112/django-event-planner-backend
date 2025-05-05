from django.contrib import admin
from .models import Event, Attendancing, Notes

# Register your models here.
admin.site.register(Event)
admin.site.register(Attendancing)
admin.site.register(Notes)

