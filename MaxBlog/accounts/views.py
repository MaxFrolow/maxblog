from braces.views import AnonymousRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView, UpdateView
from accounts.forms import LoginForm , CustomUserCreationForm , CustomUserUpdateForm
from .models import User



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

    def urlsafe_encode64(bin):
        strict_encode64(bin).tr("+/", "-_").tr('=', '')
        end

    def urlsafe_decode64(str):
        str = str.tr("-_", "+/")
        str = str.ljust((str.length + 3) & ~3, '=')
        strict_decode64(str)
        end

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        current_site = '0.0.0.0:8080'
        mail_subject = 'Activate your blog account.'
        message = render_to_string('accounts/acc_active_email.html', {
            'user': self.object,
            'domain': current_site,
            'uid': self.object.pk,
            'token': account_activation_token.make_token(self.object),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('Please confirm your email address to complete the registration')



def activate(request, uidb64, token):
    try:
        uid = uidb64
    except Exception as e:
        user = None
        return HttpResponse(uidb64)

    try:
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
        return HttpResponse('user.id')
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account. <a>http://0.0.0.0:8080/login</a>' )
    else:
        return HttpResponse('Activation link is invalid!')



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


