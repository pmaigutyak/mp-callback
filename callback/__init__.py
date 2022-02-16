
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


def setup_settings(settings, is_prod, **kwargs):

    settings['INSTALLED_APPS'] += [
        app for app in [
            'callback',
            'captcha'
        ] if app not in settings['INSTALLED_APPS']
    ]

    settings['JAVASCRIPT'] += ['callback/modal.js']


class CallbackAppConfig(AppConfig):

    name = 'callback'
    verbose_name = _('Callback')


default_app_config = 'callback.CallbackAppConfig'
