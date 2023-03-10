from rest_framework import permissions
from rest_framework.views import Request


class AuthPermissions(permissions.BasePermission):
    def has_permission(self, req: Request, view):
        try:
            if req.method in permissions.SAFE_METHODS:
                return True
            return req._user.is_colaborator
        except:
            return False


class EnsureExistPermissions(permissions.BasePermission):
    def has_permission(self, req: Request, view):
        try:
            if not req._auth:
                return False
            return True
        except:
            return False
