from venv import create

from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework import generics, status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        AllowAny,
                                        IsAdminUser,
                                        DjangoModelPermissions,
                                        BasePermission,
                                        SAFE_METHODS)

class Perms(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in ('GET', 'OPTIONS'):
            return True
        elif (request.user.is_authenticated and request.user == obj.asignee and
              request.method in ('GET', 'OPTIONS', 'PUT')):
            return True





class TaskListApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = []

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.player = self.request.user
        instance.save()

class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer





