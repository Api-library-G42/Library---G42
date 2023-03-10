from rest_framework import permissions
from rest_framework.views import Request, View
from book.models import Book


class IsColaborator(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, pk: Book):
        if request.user.is_authenticated and request.user.is_colaborator == False:
            return False
        if request.user.is_authenticated and request.user.is_colaborator == True:
            return True
