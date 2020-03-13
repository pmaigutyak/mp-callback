
from django import forms

from captcha.fields import ReCaptchaField

from callback.models import Callback
from callback.widgets import TimeSelect


class CallbackForm(forms.ModelForm):

    captcha = ReCaptchaField()

    class Meta:

        model = Callback

        fields = [
            'answer_time', 'answer_start_time', 'answer_end_time', 'comment',
            'mobile'
        ]

        widgets = {
            'answer_time': forms.RadioSelect,
            'answer_start_time': TimeSelect,
            'answer_end_time': TimeSelect
        }
