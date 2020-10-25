from django.urls import path
from to_do.views import BoardListAPIView, BoardCreateAPIView, BoardUpdateDestroyAPIView

urlpatterns = [
    path('board-list/', BoardListAPIView.as_view()),
    path('board-create/', BoardCreateAPIView.as_view()),
    path('board-rud/<int:pk>', BoardUpdateDestroyAPIView.as_view()),

]
