
from django.contrib import admin

from callback.models import Callback


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'mobile', 'comment', 'date_created', 'user',
    ]

    list_display_links = ['id', 'mobile']

    search_fields = ['mobile']

