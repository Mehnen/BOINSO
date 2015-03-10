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
