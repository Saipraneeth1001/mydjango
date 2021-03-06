from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "email", "password1", "password2")
        model = get_user_model()
# get_user_model() gives us the current user model ...
# super() method is called to display it in the form of a tuple..
# label method id to over ride the display format

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


# the above form is defined to perform a signup function
# used by the user to fill the data and submit to signup
# this form inherits from user creation form i.e django's in built ..
