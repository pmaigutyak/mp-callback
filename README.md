# MP-callback

Django callback app.

### Installation

Install with pip:

```
pip install django-mp-callback
```

Add `callback` to `INSTALLED_APPS`

Add js script `callback/modal.js`

Add url `path('callback/', include('callback.urls')),`

Add script `new CallbackModal('{% url 'callback:modal' %}');`

Add admin item `ChildItem(model='callback.callback')`

### Requirements

App require this packages:

* django-recaptcha
* django-widget-tweaks
