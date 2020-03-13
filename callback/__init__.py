
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CallbackAppConfig(AppConfig):

    name = 'callback'
    verbose_name = _('Callback')


default_app_config = 'callback.CallbackAppConfig'
