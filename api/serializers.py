from django.contrib.auth.models import User
from rest_framework import serializers


class SignUpSerializer(serializers.ModelSerializer):

    """
    Serializer that takes/returns OAuth2
    application client_id and client_secret.
    Used to sign up new users.
    """

    client_id = serializers.SerializerMethodField()
    client_secret = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('username', 'email',
                  'password', 'client_id',
                  'client_secret')
        write_only_fields = ('password')

    def get_client_id(self, obj):
        return obj.application_set.first().client_id

    def get_client_secret(self, obj):
        return obj.application_set.first().client_secret

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(SignUpSerializer):

    """
    Used for initial log in (still http basic).
    Returns client_id and client_secret
    which in turn can be used to request OAuth2 token.
    """

    class Meta:
        model = User
        fields = ('client_id', 'client_secret')


class UserSerializer(serializers.HyperlinkedModelSerializer):

    """
    Basic user serializer exposing Djangos core authentication user model.
    """

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
        write_only_fields = ('password',)

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
