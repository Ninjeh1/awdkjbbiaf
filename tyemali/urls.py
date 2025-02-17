from django.urls import path
from . import views

urlpatterns = [
    path('penlebi/', views.PenaliListApiView.as_view()),
    path('penlebi/<int:pk>/', views.PenaliDetailApiView.as_view())
]
