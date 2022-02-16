
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from callback.views import CreateCallbackView


app_name = 'callback'


urlpatterns = [

    path('', CreateCallbackView.as_view(), name='modal')

]

app_urls = i18n_patterns(

    path('callback/', include((urlpatterns, app_name)))

)
