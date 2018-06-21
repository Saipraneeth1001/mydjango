from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout


from accounts import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
