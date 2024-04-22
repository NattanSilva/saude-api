from rest_framework import permissions
from rest_framework.views import Request, View

from ..models import Professional


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(
        self, request: Request, view: View, obj: Professional
    ) -> bool:
        return (
            request.user.is_authenticated
            and (obj == request.user)
            or (request.user.is_staff)
        )
