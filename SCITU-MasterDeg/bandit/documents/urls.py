from django.conf.urls import url
from . import views

urlpatterns = [
    # /documents/
    url(r'^$' , views.index ),
    # /documents/etc
    url(r'^(?P<form_id>[0-9])/$',views.detail_form, name='detail_form'),
]
