from rest_framework import serializers
from reminder.models import Reminder

class ReminderListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'