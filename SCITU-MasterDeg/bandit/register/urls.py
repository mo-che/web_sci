from django.conf.urls import url
from . import views

urlpatterns = [
    #default
    url(r'^$' , views.index ),
    url(r'^regupload' , views.reg_upload, name="regupload" ),
    url(r'^regdel/(?P<reg_id>[0-9]+)' , views.reg_delete, name="regdel" ),
    #/something
    url(r'^(?P<reg_id>[0-9]+)/$',views.detail_reg, name='detail_reg')

]
