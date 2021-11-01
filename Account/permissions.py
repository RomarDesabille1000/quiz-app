from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj == request.user:
            return True

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.type == 2:
            return True
