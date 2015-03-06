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
    API root view. Gives back urls to all endpoint roots.
    """

    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
        }
    )


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    paginate_by = 100


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
