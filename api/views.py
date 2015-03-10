from django.contrib.auth.models import User

from api.serializers import UserSerializer, SignUpSerializer, LoginSerializer
from api.permissions import IsAuthenticatedOrCreate

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import BasicAuthentication

from oauth2_provider.ext.rest_framework import OAuth2Authentication, TokenHasReadWriteScope


@api_view(('GET',))
def api_root(request, format=None):
    """
    API root endpoint.
    Gives information about all available Endpoint branches.
    """

    return Response(
        {
            'users': reverse('user-list', request=request, format=format),
            'sign-up': reverse('sign-up', request=request, format=format),
            'login': reverse('login', request=request, format=format)
        }
    )


class SignUp(generics.CreateAPIView):

    """
    Endpoint for signing up new users.
    Returns client_id and client_secret for initial OAuth2 token request.
    """

    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticatedOrCreate,)


class Login(generics.ListAPIView):

    """
    Login endpoint for existing users.
    Returns client_id and client_secrete for subsequent OAuth2 token requests.
    Only part of the application that still requires HTTP Basic Authentication.
    """

    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return [self.request.user]


class UserList(generics.ListCreateAPIView):

    """
    Generic user list endpoint.
    Authenticated users see all user accounts and may create new users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)
    paginate_by = 100


class UserDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Generic user detail endpoint.
    Authenticated users see the details of one distinct user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)
