from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=254, unique=True, verbose_name=_('user email'), db_index=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_('phone number'), db_index=True)
    full_name = models.CharField(max_length=300, blank=True, null=True, verbose_name=_('full name'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

