from django.conf.urls import url
from . import views

urlpatterns = [
    # /public/
    url(r'^public/$' , views.news_public ),
    # /fund/
    url(r'^fund/$' , views.news_fund ),
    # /public/etc
    url(r'^public/(?P<public_id>[0-9]+)/$',views.detail_public, name='detail_public'),
    # /fund/etc
    url(r'^fund/(?P<fund_id>[0-9]+)/$',views.detail_fund, name='detail_fund')



]
