from rest_framework.permissions import BasePermission


class IsSellerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return bool(request.user and getattr(request.user, 'is_seller', False))