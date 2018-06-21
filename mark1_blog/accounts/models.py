from django.contrib import auth
from django.contrib.auth import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
