from oauth2_provider.models import Application
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def create_auth_client(sender, instance=None, created=False, **kwargs):
    """
    Creates OAuth2 Application object with
    client_id and client_secret for newly generated users.
    """
    if created:
        Application.objects.create(
            user=instance,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_PASSWORD)


post_save.connect(create_auth_client, sender=User, dispatch_uid="sign_up_user")
