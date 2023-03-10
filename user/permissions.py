from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, obj, pk):
        return request.user.is_authenticated and pk == request.user
