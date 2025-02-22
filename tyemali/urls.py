from django.urls import path
from . import views

urlpatterns = [
    path('Task/', views.TaskListApiView.as_view()),
    path('Task/<int:pk>/', views.TaskDetailApiView.as_view())
]
