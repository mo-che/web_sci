from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    # /documents/
    url(r'^$' , views.index ),
    # /documents/etc
    url(r'^(?P<form_id>[0-9])/$',views.detail_form, name='detail_form'),
    url(r'^uploadfile/' , views.model_document_upload ,name='uploadfile' ),
    url(r'^uploadengdoc/' , views.model_EngDocument_upload ,name='uploadEngdocfile' ),
    url(r'^uploadform/' , views.model_form_upload ,name='uploadform' ),
    url(r'^documentdel/(?P<id>[0-9]+)' , views.document_delete, name="documentdel" ),
    url(r'^formdel/(?P<id>[0-9]+)' , views.form_delete, name="formtdel" ),
    url(r'^engdocdel/(?P<id>[0-9]+)' , views.engDoc_delete, name="engdocdel" ),



]
