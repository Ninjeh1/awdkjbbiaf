from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework import generics, status
from .models import Penali
from .serializers import PenaliSerializer
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        AllowAny,
                                        IsAdminUser,
                                        DjangoModelPermissions,
                                        BasePermission,
                                        SAFE_METHODS)

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or
                    request.user and
                    request.user.is_staff
                    )


class PenaliListApiView(generics.ListCreateAPIView):
    queryset = Penali.objects.all()
    serializer_class = PenaliSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.player = self.request.user
        instance.save()

class PenaliDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Penali.objects.all()
    serializer_class = PenaliSerializer
    permission_classes = [DjangoModelPermissions]





