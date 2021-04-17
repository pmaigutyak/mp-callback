
class CallbackSettings(object):

    @property
    def JAVASCRIPT(self):
        return super().JAVASCRIPT + (
            'callback/modal.js',
        )

    @property
    def INSTALLED_APPS(self):
        apps = super().INSTALLED_APPS + [
            'callback'
        ]

        if not 'captcha' in apps:
            apps += ['captcha']

        return apps


default = CallbackSettings
