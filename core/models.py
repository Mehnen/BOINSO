from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    latitude = models.FloatField(default=51.483462)
    longitude = models.FloatField(default=0.0586198)
    altitude = models.FloatField(default=45)

    def __str__(self):
        return "{} {}".format(self.user.username, self.user.email)
