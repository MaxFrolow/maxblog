from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser ,PermissionsMixin):
    email = models.EmailField (_('email address'), unique=True)
    first_name = models.CharField (_('first name'), max_length=25)
    last_name = models.CharField (_('last name'), max_length=25)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', null=True, blank=True, default='static/index.png')
    is_staff = models.BooleanField(_('staff'), default=True)
    is_active = models.BooleanField(_('active'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    @property
    def get_short_name(self):

        return self.first_name