from django.urls import path
from to_do.views import BoardListAPIView, BoardCreateAPIView, BoardUpdateDestroyAPIView, TodoCreateApiView, \
    TodoListApiView, TodoDeleteApiView, TodoListUnDoneApiView, TodoUpdateApiView

urlpatterns = [
    path('board-list/', BoardListAPIView.as_view()),
    path('board-create/', BoardCreateAPIView.as_view()),
    path('board-rud<int:pk>', BoardUpdateDestroyAPIView.as_view()),

    path('todo-create', TodoCreateApiView.as_view()),
    path('todo-list/<int:board>', TodoListApiView.as_view()),
    path('todo-list-undone/<int:board>', TodoListUnDoneApiView.as_view()),
    path('todo-delete/<int:pk>', TodoDeleteApiView.as_view()),
    path('todo-update/<int:pk>', TodoUpdateApiView.as_view()),

]