from django.conf.urls import url
from . import views

urlpatterns = [
    #default
    url(r'^$' , views.index ),
    #/something
    url(r'^(?P<reg_id>[0-9]+)/$',views.detail_reg, name='detail_reg')



]
