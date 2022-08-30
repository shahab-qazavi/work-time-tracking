from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class Tasks(models.Model):
    TODO = 'TD'
    IN_PROGRESS = 'PR'
    PENDING = 'PN'
    CANCEL = 'CL'
    DONE = 'DN'
    STATE_CHOICES = [
        (TODO, _('to do')),
        (IN_PROGRESS, _('in progress')),
        (PENDING, _('pending')),
        (CANCEL, _('cancel')),
        (DONE, _('done'))
    ]
    assignment = models.ForeignKey(to=User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name=_('user'))
    title = models.CharField(max_length=150, verbose_name=_('title'))
    description = models.CharField(max_length=350, blank=True, null=True, verbose_name=_('description'))
    total_hours_time = models.FloatField(default=0)
    state = models.CharField(max_length=2, default=TODO, choices=STATE_CHOICES, verbose_name=_('state'))
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))

    def __str__(self):
        return self.title
