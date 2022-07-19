from rest_framework.permissions import BasePermission

class IsArtista(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.perfil.is_artista
        )