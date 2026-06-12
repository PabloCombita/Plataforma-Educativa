from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):
    """
    Permite acceso solo a usuarios administradores.
    En este proyecto se considera admin a usuarios con is_staff=True o is_superuser=True.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.is_superuser)
        )


class IsStudentRole(BasePermission):
    """
    Permite acceso a usuarios autenticados que no son administradores.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and not request.user.is_staff
            and not request.user.is_superuser
        )