from django.urls import path
from reminder.views import ReminderListAPIView, ReminderCreateAPIView, ReminderDeleteAPIView

urlpatterns = [
    path('reminder-list/', ReminderListAPIView.as_view()),
    path('reminder-create/', ReminderCreateAPIView.as_view()),
    path('reminder-delete/<int:pk>', ReminderDeleteAPIView.as_view()),

]