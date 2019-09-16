from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):
    username = UsernameField(
        max_length = 40,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'input form-control',
                'placeholder':'Your Email'
            }
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'input form-control',
                'placeholder':'Password'
            }
        ),
    )


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip = False,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control input'
            }
        ),
    )

    password2 = forms.CharField(
        label=_("Confirm Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
    )

    first_name = forms.CharField(
        label = _("First name"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input'
            }
        ),
    )

    last_name = forms.CharField(
        label = _("Last name"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input'
            }
        ),
    )

    email = forms.CharField(
        label = _("Email"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input'
            }
        ),
    )




    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')


class CustomUserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label=_("First name"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input'
            }
        ),
    )

    last_name = forms.CharField(
        label=_("Last name"),
        strip=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input'
            }
        ),
    )

    avatar = forms.ImageField(
        label=_("Image"),
        widget=forms.FileInput(),
        required=False
    )

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "avatar")