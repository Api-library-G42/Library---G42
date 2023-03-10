from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, obj, pk):
        return request.user.is_authenticated and pk == request.user


class IsColaboratorHasPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if (
            request.method == "GET"
            and request.user.is_authenticated
            and request.user.is_colaborator == True
        ):
            return True
        if request.method == "POST":
            return True
