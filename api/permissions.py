from rest_framework import permissions


class IsAuthenticatedOrCreate(permissions.IsAuthenticated):

    """
    HTTP POST queries may pass even for unauthenticated users.
    Authenticated user may use all HTTP commands.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return super(IsAuthenticatedOrCreate, self).has_permission(
            request, view)


class IsProfileOwner(permissions.BasePermission):

    """
    Only the user has permission to work with his own userprofile via the api.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsUser(permissions.BasePermission):

    """
    Only the user can work with his own data
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
