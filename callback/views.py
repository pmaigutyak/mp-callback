
from django.conf import settings
from django.apps import apps
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from callback.forms import CallbackForm


class CreateCallbackView(FormView):

    form_class = CallbackForm
    template_name = 'callback/modal.html'

    def get_initial(self):

        user = self.request.user

        if user.is_authenticated:
            return {'mobile': self.get_user_mobile(user)}

        return self.initial

    def form_valid(self, form):

        obj = form.save(commit=False)

        if self.request.user.is_authenticated:
            obj.user = self.request.user

        obj.save()

        self.send_email_notification(obj)
        self.send_sms_notification(obj)

        message = render_to_string(
            'callback/success_message.html', {'object': obj})

        return HttpResponse(message)

    def form_invalid(self, form):
        return render(
            self.request, 'callback/form.html', {'form': form}, status=403)

    def send_email_notification(self, obj):

        context = self.get_notifications_context(obj)

        subject = render_to_string('callback/email/subject.txt', context)

        html = render_to_string('callback/email/message.html', context)

        send_mail(
            subject=subject.strip(),
            message='',
            from_email=settings.DEFAULT_FROM_EMAIL,
            html_message=html,
            recipient_list=self.get_email_recipients())

    @staticmethod
    def get_user_mobile(user):
        try:
            return user.profile.mobile if hasattr(user, 'profile') else ''
        except Exception:
            pass
        
        return ''

    @staticmethod
    def get_email_recipients():
        return [a[1] for a in settings.MANAGERS]

    def send_sms_notification(self, obj):

        if not apps.is_installed('turbosms'):
            return

        from turbosms.lib import send_sms_from_template

        context = self.get_notifications_context(obj)

        send_sms_from_template('callback/sms.txt', context)

    @staticmethod
    def get_notifications_context(obj):
        return {
            'object': obj,
            'site': apps.get_model('sites', 'Site').objects.get_current()
        }
