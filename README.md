# MP-callback

Django callback app.

### Installation

Install with pip:

```
pip install django-mp-callback
```

Add `callback` to `INSTALLED_APPS`

Add url `path('callback/', include('callback.urls')),`

Add admin item `ChildItem(model='callback.callback')`

### Requirements

App require this packages:

* django-recaptcha
* django-mp-email
* django-widget-tweaks
