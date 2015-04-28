from django.contrib.auth.models import User

from api.serializers import (UserSerializer, SignUpSerializer, LoginSerializer,
                             UserProfileSerializer)
from api.permissions import IsAuthenticatedOrCreate

from core.models import UserProfile

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authentication import BasicAuthentication

from oauth2_provider.ext.rest_framework import (
    OAuth2Authentication, TokenHasReadWriteScope
)


@api_view(('GET',))
def api_root(request, format=None):
    """
    API root endpoint.
    Gives information about all available Endpoint branches.
    """

    return Response(
        {
            'sign-up': reverse('sign-up', request=request, format=format),
            'login': reverse('login', request=request, format=format),
            'user-profile-proxy': reverse(
                'user-profile-proxy', request=request, format=format),
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


class UserProfileProxy(generics.ListAPIView):

    """
    Narrows down the search for a user via his authentication.
    Authenticated user sees his own profile and can update it.
    """

    serializer_class = UserProfileSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)

    def get_queryset(self):
        """
        This view should only get the profile of the authenticated user.
        """

        user = self.request.user
        return UserProfile.objects.filter(user=user)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    Detail view for UserProfile.
    Authenticated can update or destroy their Profiles.
    """

    serializer_class = UserProfileSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)


class UserList(generics.ListCreateAPIView):

    """
    Generic user list endpoint.
    Authenticated users see all user accounts and may create new users.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)


class UserDetail(generics.RetrieveUpdateAPIView):

    """
    Generic user detail endpoint.
    Authenticated users see the details of one distinct user.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (OAuth2Authentication,)
    permission_classes = (IsAuthenticated, TokenHasReadWriteScope)
