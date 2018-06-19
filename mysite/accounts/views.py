from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

# template name helps django to redirect when  this class is called..
# success_url redirects once the process is a success
# form_class is used to tell djagno that the form should look like that model ...


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

