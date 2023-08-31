
from django import forms
from captcha.fields import ReCaptchaField
from callback.models import Callback


class CallbackForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:

        model = Callback

        fields = [
            'comment',
            'mobile'
        ]
