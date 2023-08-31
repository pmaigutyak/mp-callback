
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Callback(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='return_calls',
        verbose_name=_('User'), blank=True, null=True,
        on_delete=models.SET_NULL)

    mobile = models.CharField(_("Mobile"), max_length=21)

    date_created = models.DateTimeField(
        _('Date created'), auto_now_add=True, editable=False)

    comment = models.TextField(_('Comment'), max_length=2048, blank=True)

    def __str__(self):
        return self.mobile

    class Meta:
        verbose_name = _('Callback')
        verbose_name_plural = _('Callbacks')
