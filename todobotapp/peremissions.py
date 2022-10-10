from rest_framework import permissions


class IsAdminUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.has_object_permission(request.request, view, obj)
