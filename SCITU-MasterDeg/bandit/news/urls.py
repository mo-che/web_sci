from django.conf.urls import url
from . import views

urlpatterns = [
    # /public/
    url(r'^public/$' , views.news_public ),
    url(r'^publicupload/$' , views.public_upload ,name="publicupload"),
    # /fund/
    url(r'^fund/$' , views.news_fund),
    url(r'^fundupload/$' , views.fund_upload,name="fundupload"  ),
    # /public/etc
    url(r'^public/(?P<public_id>[0-9]+)/$',views.detail_public, name='detail_public'),
    # /fund/etc
    url(r'^fund/(?P<fund_id>[0-9]+)/$',views.detail_fund, name='detail_fund'),
    url(r'^publicdel/(?P<id>[0-9]+)' , views.public_delete, name="publicdel" ),
    url(r'^funddel/(?P<id>[0-9]+)' , views.fund_delete, name="funddel" ),



]
