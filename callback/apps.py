
from django.apps import AppConfig, apps
from django.utils.translation import gettext_lazy as _


class CallbackAppConfig(AppConfig):

    name = 'callback'
    verbose_name = _('Callback')

    def ready(self):
        if not apps.is_installed('captcha'):
            raise Exception('`mp-callback` depends on `django-recaptcha`')

        if not apps.is_installed('djmail'):
            raise Exception('`mp-callback` depends on `djmail`')

        if not apps.is_installed('modal'):
            raise Exception('`mp-callback` depends on `django-mp-modal`')
