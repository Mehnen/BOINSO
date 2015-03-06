from django.contrib.auth.models import User
from api.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(('GET',))
def api_root(request, format=None):
    """
    API root view.

    Returns:
        Links to all other api enpoint roots.
    """

    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
        }
    )


class UserList(generics.ListCreateAPIView):

    """
    Generic user list endpoint.

    Returns:
        List of available users if requesting party is authorized
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Generic user detail endpoint.

    Returns:
        Details about a single user if requesting party is authorized.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
