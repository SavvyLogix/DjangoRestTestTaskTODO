from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ReminderListSerializers
from .models import Reminder

class ReminderListAPIView(generics.ListAPIView):
    '''
    API to get the list of all reminders
    permission: admin only.
    '''
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser,]

class ReminderCreateAPIView(generics.CreateAPIView):
    '''
    API to create a new reminder
    permission: admin only.
    '''
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser,]

class ReminderDeleteAPIView(generics.DestroyAPIView):
    '''
    API to delete reminder
    permission: admin only.
    '''
    queryset = Reminder.objects.all()
    serializer_class = ReminderListSerializers
    permission_classes = [permissions.IsAdminUser,]