
from django.db import models
from django.contrib import admin

from callback.models import Callback
from callback.widgets import TimeSelect


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'mobile', 'comment', 'get_answer_time_display',
        'answer_start_time', 'answer_end_time', 'date_created', 'user',
    ]

    list_display_links = ['id', 'mobile']

    list_filter = ['answer_time']

    search_fields = ['mobile']

    formfield_overrides = {
        models.TimeField: {'widget': TimeSelect}
    }
