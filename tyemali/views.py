from rest_framework import generics
from rest_framework.permissions import BasePermission
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        AllowAny,
                                        IsAdminUser,
                                        DjangoModelPermissions,
                                        BasePermission,
                                        SAFE_METHODS)


class Perms(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in ['GET', 'POST']:
                return True
            elif request.method == 'DESTROY':
                return request.user.is_superuser
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.method in ['GET', 'OPTIONS']:
            return True
        elif request.user.is_authenticated and request.user == obj.asignee:
            return request.method in ['PUT', 'PATCH']
        elif request.user.is_superuser and request.method in ['DESTROY','GET', 'OPTIONS']:
            if request.method == 'DESTROY':
                return True
        return False

class TaskListApiView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [Perms]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.player = self.request.user
        instance.save()

class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [Perms]





