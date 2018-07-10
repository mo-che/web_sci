from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$' , views.index ),
    url(r'^meetingupload' , views.meeting_upload , name="meetingupload"),
    url(r'^reportupload' , views.report_upload, name="reportupload" ),
    url(r'^meetdel/(?P<id>[0-9]+)' , views.meet_delete, name="meetdel" ),
    url(r'^reportdel/(?P<id>[0-9]+)' , views.report_delete, name="reportdel" ),

]
