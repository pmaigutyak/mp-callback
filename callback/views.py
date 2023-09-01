from django.apps import apps
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _
from djmail import mail_managers

from callback.forms import CallbackForm
from modal.views import ModalFormView


class CreateCallbackView(ModalFormView):

    form_class = CallbackForm
    template_name = 'callback/modal.html'

    def get_initial(self):

        user = self.request.user

        if user.is_authenticated and hasattr(user, 'profile'):
            return {**self.initial, 'mobile': user.profile.mobile}

        return self.initial

    def save_form(self, form):

        referrer = self.request.GET.get("referrer", "")

        obj = form.save(commit=False)

        if referrer:
            site = Site.objects.get_current()
            obj.comment += f"\nhttps://{site.domain}{referrer}"

        if self.request.user.is_authenticated:
            obj.user = self.request.user

        obj.save()

        subject = '%s #%s' % (_("New callback request"), obj.id)

        html = render_to_string('callback/email.html', {
            'object': obj,
            'site': Site.objects.get_current()
        })

        mail_managers(subject, html)

        if apps.is_installed('turbosms'):
            from turbosms import send_sms
            send_sms('%s #%s %s' % (_('Callback'), obj.id, obj.mobile))

        return obj

    def get_success_context(self, obj):
        return {
            "message": _('Callback request was successfully sent')
        }

