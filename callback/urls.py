
from django.urls import path

from callback.views import CreateCallbackView


app_name = 'callback'


urlpatterns = [

    path('', CreateCallbackView.as_view(), name='modal')

]
