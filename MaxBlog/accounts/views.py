from braces.views import AnonymousRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView

from accounts.forms import LoginForm , CustomUserCreationForm , CustomUserUpdateForm



class CustomLoginView(SuccessMessageMixin, AnonymousRequiredMixin, LoginView):
    template_name = 'accounts/login.html'
    success_url = '/'
    form_class = LoginForm
    success_message = _('You are successfully logged in')


class CustomLogoutView(LogoutView):
    next_page = '/'

class RegisterCreateView(AnonymousRequiredMixin, CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    template_name = "accounts/registration.html"

    def __init__(self):
        super().__init__()
        self.avatar = "media/avatarts/index.html"


    def get_success_url(self):
        return reverse_lazy('accounts:login')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'accounts/registration.html'
    success_url = '/'
    form_class = CustomUserUpdateForm
    succes_message = _('Updated')

    def get_queryset(self):
        return self.model.objects.filter(id=self.request.user.id)
    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context.update({'btn_text': _('Update')})
        return context


