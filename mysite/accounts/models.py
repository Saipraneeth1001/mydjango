from django.contrib import auth
from django.contrib.auth import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

# this model is only to define the form that is signup form !
# used in the later section in forms.py file
# now this user class inherits from the auth.model.User i.e built in django user .
